def post_template(name: str, content: str, ext: str = "py") -> str:
    """
    Template for all posts on the website.

    Arguments:
        name (str): title of the post
        content (str): html string containing the body of the post
        ext (str): file extension for the bottom vim-like status top-bar
            Only for aesthetic purposes
            Defaults to "py"

    Return:
        (str): final html markup for a post page
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/styles/style.css">
    <link rel="stylesheet" href="/styles/post.css">
    <link rel="stylesheet" href="/styles/lifeline.css">
    <link rel="stylesheet" href="/styles/topbar.css">
    <title>{name}</title>
    <base target="_blank">
</head>
<body>
    <div class="top">
        <div class="top-txt" ><a href="/index.html" target="_self">Force</a></div>
        <div class="top-bar">
            <span class="top-btn min"></span>
            <span class="top-btn max"></span>
            <span class="top-btn close"></span>
        </div>
    </div>
    <main>
        {content}
    </main>

    <div class="life-line">
        <div class="line">
            <span class="life-line-start">
                <span class="life-line-color">█</span>
                {name}.{ext}
            </span>

        </div>
    </div>
</body>
</html>"""
