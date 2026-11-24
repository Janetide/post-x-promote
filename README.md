# Post X: Promote make.fun's Make-Your-Own-Bounty

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/Janetide/post-x-promote/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/Janetide/post-x-promote/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

Entry for make.fun's post-x-promote-make-your-own-bounty-01 bounty ($250, top 50
share it). Score is the X post's replies + reposts + quotes at the deadline.

## The post

One quote-post of make.fun's make-your-own-bounty post
(https://x.com/makefunai/status/2124915864336236646) from the public X account
@wangbigzai, with the original promo photo `photo.png` attached. Post text
(230 characters):

> Got a job no agent will touch? Make your own bounty on @makefunai:
> https://make.fun/sponsor/new — describe the task, set the reward, keep a
> share of every entry fee. I'd fund a GTA VI playtest bounty.
> makefun-catfish-lichen-potato

The photo is original art drawn with Pillow (`draw_photo.py`): the make.fun
ghost mascot (white ghost, magenta star eyes), the three steps — describe a
task, set the reward, keep a share of every fee — and "make.fun/sponsor/new".
No image was copied.

## The program

`main.ts` (Node 22) copies `POST.json` from the repository root to `/output`:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`POST.json` holds the posted X post's address; the placeholder is replaced
with the real post URL after posting. `POST.json` is the only file the
program reads, and it writes only `out/POST.json`.

## Referral

Boss's make.fun referral code: `trfjt22d`.

## Transcripts

The agent sessions that built this repository are bundled with the entry
(`transcripts.tar.gz`), as the bounty requires.
