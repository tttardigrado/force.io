def index_template(posts: str) -> str:
    """
    template for the "index.html" page of the website

    Arguments:
        posts (str): html string containing a list of topics
          this topics should contain the related series
          and those series should contain the path to their related posts
          -> ex:
                <li><details>
                    <summary>Music</summary>
                    <li><details>
                        <summary>Playlists</summary>
                        <li><a href="path/to/post1">Playlist1</a></li>
                        <li><a href="path/to/post2">Playlist2</a></li>
                    </detail></li>
                    <li><details>
                        <summary>Reviews</summary>
                        <li><a href="path/to/reviews1">Review1</a></li>
                        <li><a href="path/to/reviews2">Review2</a></li>
                    </detail></li>

                </details></li>
    Return:
        (str): full html markup for the site's "index.html" file
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/style.css">
    <link rel="stylesheet" href="styles/lifeline.css">
    <link rel="stylesheet" href="styles/topbar.css">
    <title>🪐 Tardigrade</title>
</head>
<body>
    <div class="top">
        <div class="top-txt" ><a href="/index.html" target="_self" >Tardigrade</a></div>
        <div class="top-bar">
            <span class="top-btn min"></span>
            <span class="top-btn max"></span>
            <span class="top-btn close"></span>
        </div>
    </div>

    <img class="bg-img" src="assets/bg.png">

    <main>
        <h1>Tardigrade's World</h1>
        <hr>
        <h2>Who Am I?</h2>
        <div class="who">
            <p>Hi! 🖖</p>
            <p>My name is <em>Gonçalo Teixeira</em>, also known around the corners of the web as <strong>Tardigrade</strong> </p>
            <p>I'm a Portuguese <strong>🪐 physics</strong> student at <em>Universidade do Porto</em></p>
            <p>This is my personal website where you will be able to find a lot of posts about what I enjoy doing.</p>
            <p>My interests range from <strong>💻 Computer Science</strong>, <strong>🎶 Music</strong>, <strong>🪐 Sci-fi</strong> and <strong>📚 Debates</strong></p>

        </div>
        <hr>
        <h2>Posts</h2>
        <ul class="posts">
        {posts}
        </ul>
        <hr>
        <h2>Links</h2>
        <p><a href="https://www.instagram.com/_tardigrado_/" target="_blank"> 📷 Instagram</a></p>
        <p><a href="https://soundcloud.com/g-force-beats" target="_blank"> 🎶 SoundCloud</a></p>
        <p><a href="https://github.com/Force4760" target="_blank"> 💻 GitHub</a></p>
        <hr>
    </main>

    <div class="life-line">
        <div class="line">
            <span class="life-line-start">
                <span class="life-line-color">█</span>
                tardigrade.py
            </span>
        </div>
    </div>
</body>
</html>"""
