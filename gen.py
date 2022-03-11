import json
import shutil
import os
from mdit_py_plugins import footnote, tasklists, texmath, anchors 
from markdown_it import MarkdownIt
from pathlib import Path
import templates
import random


# path to the most important folders
# src, build and content
# edit if you want to store them somewhere else
src_path: str = "./src"
content_path: str = os.path.join(src_path, "content")
build_path: str = "./build"


# MarkdownIt object that will parse the markdown posts into html
md: MarkdownIt = (
    MarkdownIt()
    .use(anchors.anchors_plugin)
    .use(footnote.footnote_plugin)
    .use(tasklists.tasklists_plugin)
    .use(texmath.texmath_plugin)
)


# list of some common extensions for some popular
# programming languages or file formats
# only for aesthetic reasons
file_extensions: list = [
    "py",
    "c",
    "js",
    "go",
    "hs",
    "lua",
    "vim",
    "emacs",
    "jl",
    "pd",
    "rs",
    "sh",
]


def file_name(path: str) -> str:
    """
    Get the name of the post file
        ex: path/to/some/post/file.md -> file
        ex: path/to/some/other/file/with/a/post.html -> post

    Arguments:
        path (str): path to the file

    Return:
        (str): name of the file
    """
    return os.path.basename(path).split(".")[0]


def get_extension() -> str:
    """
    Get a random extension from the ones provided

    Return:
        (str): file extension
    """
    return random.choice(file_extensions)


def process_content(content: str, path: str) -> None:
    """
    Process the content of a post, turn it into html and reder it to a file

    Arguments:
        content (str): markdown content of the post
        path (str): path to the md file
    """

    # turn markdown to html
    html_text = md.render(content)

    # get the name of the post file
    # ex: path/to/some/post/file.md -> file
    name = file_name(path)

    # create a random extension
    ext = get_extension()

    # get the final html for the post using the predefined template
    html_text = templates.post_template(name.capitalize(), html_text, ext)

    # make the path
    file_path: str = f"{name}.html"
    file_path = os.path.join(build_path, "content", file_path)

    # create the final post html file
    Path(file_path).write_text(html_text)


def make_post(path: str) -> str:
    """
    process and create a post

    Arguments:
        path (str): path to the markdown file containing the post content

    Return:
        (str): name of the post
    """
    # read the post
    with open(os.path.join(content_path, path), "r") as f:
        content = f.read()
        process_content(content, path)

    # get the name of the file
    return file_name(path)


def copy() -> None:
    """
    Copy the non-generated (i.e. assets, style sheets (css) and scripts (js))
    from the source folder to the final build folder
    """
    # origin paths on the src folder
    assets_path: str = os.path.join(src_path, "assets")
    style_path: str = os.path.join(src_path, "styles")
    scripts_path: str = os.path.join(src_path, "scripts")

    # destination paths on the build folder
    build_assets: str = os.path.join(build_path, "assets/")
    build_styles: str = os.path.join(build_path, "styles/")
    build_scripts: str = os.path.join(build_path, "scripts/")

    # copy from the origin (src) to the destination (build)
    shutil.copytree(assets_path, build_assets)
    shutil.copytree(style_path, build_styles)
    shutil.copytree(scripts_path, build_scripts)


def process_series(series: dict) -> list:
    """
    Process a series of posts

    Arguments:
        series (dict): dictionary containing a name and a list of posts

    Return:
        (list): name of all episodes/posts in this series
    """
    episodes: list = []

    # process every post
    for post in series["posts"]:
        episodes.append(make_post(post))

    return episodes


def process_config(config: dict) -> str:
    """
    Process the whole config file, creating the index and every other post

    Arguments:
        config (dict): dictionary containing all the topics, series and posts

    Return:
        (str): html string with all the <details>, <li> and <a> tags
        containg the topics, series and posts
    """
    html: str = ""

    for key in config:
        html += f"<li><details><summary>{key.capitalize()}</summary>"

        for value in config[key]:
            episodes: list = process_series(value)
            html += f"<li>"

            for ep in episodes:
                html += f"<li><a href='{os.path.join('./content', ep)+'.html'}'>{ep.capitalize()}</a></li>"

            html += "</li>"

        html += "</details></li>"

    return html


def make_build_path():
    """
    Create the folder for the build of the website
    """
    # remove the previous build
    try:
        shutil.rmtree(build_path)
    except FileNotFoundError:
        # FileNotFoundError means that there is no previous
        # build folder, in that case, there is no need to remove it
        pass

    # create the build path
    os.makedirs(build_path)
    # create the content path under build
    os.makedirs(os.path.join(build_path, "content/"))
    # copy the assets, styles and scripts
    # from the src folder to the build folder
    copy()


def main():
    """
    Main function
    """
    # remove and remake the build folder
    make_build_path()

    # path to the config file
    # the config file holds the paths of the topics/series/posts
    config_path: str = os.path.join(src_path, "config.json")

    # load the contents of the config
    with open(config_path, "r") as f:
        config = json.load(f)

    # process the config file and get the html with the list of topics
    html: str = process_config(config)

    # get the final content for the index.html file
    html = templates.index_template(html)

    # write the index.html file
    Path(os.path.join(build_path, "index.html")).write_text(html)


if __name__ == "__main__":
    main()
