#!/bin/bash



# get time duration of the track
# currently not being used, but it could be usefull
#time=$(ffprobe -i $file -show_entries stream=codec_type,duration -of compact=p=0:nk=1 | grep -Po '(?<=audio\|)[0-9]*\.[0-9]*')

function install_all_dependencies(){
    sudo apt install youtube-dl ffmpeg grep sed
}

function display_help(){
    echo ""
    echo "# # # # # # # # # #"
    echo ""
    echo "  Usage:"
    echo "      * -h or --help -> displays this message"
    echo "      * -i or --install -> install all the needed dependencies"
    echo "      * name_of_a_file or name_of_a_file.extension -> reads the contents of that file, gets the markdown formated links inside of it, downloads them as audio files and mixes them into a single auido file."
    echo "          - markdown links are formated like this: [text](link), where text is the text to be shown and link is the link that the text should point to"
    echo ""
    echo "# # # # # # # # # #"
    echo ""
}


function file_does_not_exist(){
    echo "That file does not exist"
}

function init_file_structure(){
    # make a directory for this playlist
    mkdir $1

    #copy the markdown file
    cp $1'.md' $1'/'$1'.md'

    # change to the new folder
    cd $1

    # make 2 directories.
    # 1 to download the music
    # 2 to move the processed music to
    mkdir downloaded
    mkdir processed
}

function download(){
    # download the provided link from youtube to the ./downloaded folder
    youtube-dl $1 --restrict-filenames --no-playlist --extract-audio --audio-format mp3 --audio-quality 1 -o './downloaded/'$2'.%(ext)s'
}

function fade(){
    # process the provided song from the ./downloaded directory
    # remove silence (everything bellow -50dB) from the beggining and the end
    # fade in and fade 8 $2s
    ffmpeg -i './downloaded/'$1'.mp3' -filter_complex "silenceremove=start_periods=1:start_silence=0.1:start_threshold=-50dB, afade=d=$2, areverse,silenceremove=start_periods=1:start_silence=0.1:start_threshold=-50dB, afade=d=$2, areverse" './processed/'$1'.mp3' -y
}

function files_in_dir_to_txt(){
    # get all files on the directory (ls)
    # filter for mp3 files (grep)
    # change them from *file_name.extension* to file file_name.extension
    # store that into a file (files.txt), one file per line
    ls $1 | grep '.*\.mp3' | sed 's/^/file /' > $1'/files.txt'
}

function mix_songs(){
    # mix all songs into one
    # $1 is a file containg the name of all music files to mix
    # file file_name.extension
    #
    # $2 is the name of the output file
    ffmpeg -f concat -safe 0 -i $1 -c copy $2 -y
}

function get_links_from_file(){
    # create an array with the links
    # to the songs that should be downloadede
    #
    # gets all links from a markdown (.md) file
    # links in markdown are worded like:
    #       [name](__link__)
    # this grep commande gets the __link__
    song_links=( $(grep -Po "(?<=\().*(?=\))" $1'.md') )
}

function download_and_process_song(){
    download $1 $2
    fade $2 7
}

function download_all_from_file(){
    # get all links from the .md file
    get_links_from_file $1

    # song number variable
    # used to make the songs concat in the correct order
    local num=1

    # donwload and process all songs
    for i in "${song_links[@]}"
    do
        download_and_process_song $i 'song'$(printf "%02d" $num)
        let num+=1
    done
}

function file_name(){
    # get the name of the provided file
    name=$(echo "$1" | cut -f 1 -d '.')
}

function should_delete_downloaded(){
    # Ask the user if the non-processed songs
    # (i.e. the ones under ./downloaded)
    # should be deleted
    echo "\n\n###\nDo you want me to delete the non-processed songs? [y/n]"
    read DELETE
    case $DELETE in
        y | yes | Y | Yes)
            # delete songs if the answer is yes
            echo "Deleting non-processed songs"
            rm -rf ./downloaded
            ;;

        *)
            # skip deletion if the answer is no
            echo "Ok. The non-processed songs will not be deleted"
    esac
}

function main(){
    if [[ $1 == "--install" ]] || [[ $1 == "-i" ]]; then
        install_all_dependencies
    elif [[ $1 == "--help" ]] || [[ $1 == "-h" ]]; then
        display_help
    elif [[ -f "$1" ]] || [[ -f "$1.md" ]]; then
        file_name $1
        init_file_structure $name
        download_all_from_file $name
        files_in_dir_to_txt ./processed
        mix_songs ./processed/files.txt mix.mp3
        should_delete_downloaded
    else
        file_does_not_exist
    fi
}

main $1
