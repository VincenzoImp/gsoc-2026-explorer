# support more torrent clients

**Parent:** CCExtractor Development — Project Ideas
**Source:** https://ccextractor.org/public/gsoc/flutter-more-clients
**Scraped:** 2026-02-22T23:28:47.612111

---

# Extend the app to support more torrent clients

**Deluge**

[Deluge](https://deluge-torrent.org/) is a popular BitTorrent
client. It's popular because it's quite efficient and performs really
well compared to alternatives, but its web interface is terrible and the
desktop UI is not great.

However, it does have a good plugin system and writing proper alternatives with Flutter is possible and not painful, so let's go for it.

The goal is to write a flutter-based interface (web and mobile).

Start by installing deluge and its current web UI so get a feeling of how it looks like, and come up with a good replacement UI.

Read the documentation to find out which part of Deluge don't yet have a UI counterpart at all.

**Flood**

[Flood](https://flood.js.org) is a monitoring service for various torrent
clients. It's a Node.js service that communicates with your torrent
client and serves a decent web UI (in React) for administration.

Flood backend can communicate with different clients. However, it exposes one common set of API. This allows developers of an integration to support multiple torrent clients via Flood's API. On the other hand, Flood allows developers of a torrent client to quickly set up a functional UI and get supported by integrations.

Additionally, Flood supports advanced features like filesystem browsing, content streaming and RSS.

Flood's API is well documented and typed. It uses simple HTTP and JSON.
For instance, see [POST /api/torrents/add-urls endpoint](https://github.com/jesec/flood/blob/9283a1d32db5592e004f52f98c9dffdc4e7bb85a/server/routes/api/torrents.ts#L107) and
[AddTorrentByFileOptions type](https://github.com/jesec/flood/blob/d84c8aacb879d01c0e3eafeb87d3a5dfa73340fe/shared/schema/api/torrents.ts#L10).

Head maintainer of Flood, [jesec](https://github.com/jesec), is one of the
mentors. He can provide help if you have troubles setting up Flood or
encountered issues with Flood's API.

**Your task**

The task at hand is to extend Flutter app to support Deluge and/or Flood.

You should work with your peer, whose goal may be different from yours, to find a way to support multiple API integrations in one application. You can check out how Flood did it.
