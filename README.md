# DotPodcast website

This is the content for the DotPodcast website. Crucially right now
it's a place to work on things like the JSON Feed spec, but it could
grow to become a more comprehensive home for everything we want to
tell the public about the project.

Because of the public nature of GitHub, contributions to this repo are
visible to those that follow us. So the language is purposely vague
where it needs to be right now.

## Working on the site

To add or edit content on the site, you'll need Python and Virtualenv.
Clone this repo and then `cd` into the directory you cloned the repo
into. Then run the following:

```
virtualenv venv
```

This will create a directory called _venv_ which hosts a Python
environment, isolated from the rest of your Python installation and
other projects.

Now run

```
source venv/bin/activate
```

Thisi tells your computer that when you type `python` or `pip` in
the future, you're referring to this isolated instance. (To return to
your original Python installation, just run `deactivate`.)

To install the relevant packages you'll need, run

```
pip install -r requirements.txt
```

This will install Pelican, Markdown and other requirements.

When you make changes, you can run

```
make html
```

And static files will be generated in the _output_ directory.

There's a local development server which you can run, which will
watch for changes and republish the site. Run this via

```
make devserver
```

Then visit _http://localhost:8000/_ in your browser, and you should
see a copy of the site.

## Publishing to GitHub Pages

Once you've made your changes, commit them to the _master_ branch as
normal, then from your terminal, run

```
make github
```

This will publish the static files and copy them to a Git branch
called _gh-pages_, which will then be pushed to GitHub. After a few
minutes, you should see your changes at <https://dotpodcast.github.io/dotpodcast/>
