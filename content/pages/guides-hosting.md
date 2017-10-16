Title: DotPodcast for hosting providers
Slug: guides/hosting


Although DotPodcast allows content creators to host their audio and generate income directly, many will choose to use a trusted provider to handle the technical details.

Hosting providers are responsible for producing the JSON Feed, validating Bitcoin transactions that accrue when restricted content is paid for, and usually providing analytics.

## Providing the feed

Read the [JSON Feed spec](../../spec-v1) to find out how to produce a feed, and for an idea as to how you'll structure your database.

## Serving audio/video content

Serving the content files - known in traditional terms as the "enclosure" - is not as simple as providing a URL. DotPodcast hosting providers need to provide a small API that allows for the exchange of tokens, which help you tell one listener from another (and mitigate against duplicate downloads or preview listens) without sacrificing information about the actual person listening. See the guide on [subscription tokens](../../subscription-tokens).
