Title: DotPodcast for app developers
Slug: guides/apps


Podcast apps can crawl directories or maintain their own, depending on your level of skill.

## Using a third-party directory

You can partner with a directory provider and use an API they expose, to provide search capabilities to your app.

This site does not currently maintain a list of directory services.

## Building your own directory

If you want to, you can build your own directory for use only inside your app, by crawling the Blockstack `podcast` namespace, and parsing the JSON Feed that is specified in each podcast's zone file. See the [DotPodcast for directory developers](../directories) guide.

## Downloading content

Unlike traditional podcast players, your app will need to do a little more work to download content on behalf of your users. See the guide on [download tokens](../../subscription-tokens/#download-tokens).
