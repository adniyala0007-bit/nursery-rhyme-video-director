# Nursery Rhyme Video Director

An open, practical production kit for planning original nursery-rhyme videos for YouTube. It adapts the scene-by-scene director workflow of [stickman-video-director](https://github.com/kaomei/stickman-video-director) to a colorful 3D preschool world, using the user's supplied channel screenshots only as broad layout and pacing references.

**Working channel identity:** Milo & Friends (editable)  
**Recurring cast:** Milo, Lila, Pip, and Bubo  
**Default full episode:** 2 minutes, landscape 16:9  
**Shorts cutdowns:** vertical 9:16, usually 15–30 seconds

This repository is a prompt and production workflow. It does not generate music, images, voices, or finished videos by itself; use the prompts with the creative tools you choose, then assemble and review the results in your editor.

## What is inside

- **Director workflow:** turn a simple theme into an original song, timed storyboard, shot prompts, and sound notes.
- **Production-pack workflow:** prepare a complete episode handoff, including thumbnail direction, title, description, tags, and Shorts cutdowns.
- **Character and world guide:** keep the recurring cast and approved garden setting visually consistent.
- **Starter episode:** a complete, original two-minute sample, “Good Morning, Garden Friends.”
- **Episode brief generator:** create a fresh Markdown episode folder with one command; it uses only Python's standard library.

## Quick start

1. Read [`docs/channel-blueprint.md`](docs/channel-blueprint.md) and replace the working channel name if needed.
2. Read [`docs/character-bible.md`](docs/character-bible.md). Treat any marked draft details as suggestions until you approve them.
3. Open [`episodes/ep-001-good-morning-garden-friends/episode.md`](episodes/ep-001-good-morning-garden-friends/episode.md) to see the complete sample format.
4. Create a new brief:

   ```bash
   python3 scripts/new_episode.py --id ep-002 --title "The Little Rain Dance"
   ```

5. Ask an AI assistant that can read repository files:

   ```text
   Read skills/directing-nursery-rhyme-videos/SKILL.md and the channel guide.
   Use Director Mode to develop this episode brief:
   episodes/ep-002-the-little-rain-dance/episode.md
   Keep the recurring characters and world consistent. Show me the treatment
   and original lyrics first; wait for my approval before writing final shot prompts.
   ```

## Production modes

| Mode | Use it for | You receive |
| --- | --- | --- |
| A · Director Mode | Hands-on creation, usually 30 seconds–3 minutes | Creative treatment, original lyrics, timed storyboard, shot-by-shot image/video prompts, camera and sound direction |
| B · Production Pack | A ready-to-produce episode handoff | Mode A outputs plus thumbnail brief, YouTube metadata, playlist suggestion, and Shorts cutdowns |

Both modes use the same character bible, safety checks, and review gates. Generate a short visual test before making every scene; approve the character look, vocal style, and color palette before producing the full episode.

## Repository map

```text
docs/                         Channel, character, style, and workflow guides
episodes/                     Episode briefs and completed production packs
prompts/                      Reusable image, video, thumbnail, and music prompts
skills/                       Instructions for an AI assistant acting as video director
scripts/                      Small local productivity tools
templates/                    Blank episode and storyboard templates
```

## Copyright and child-directed content

Write new lyrics and melodies for this channel. Do not reproduce lyrics, melodies, character designs, logos, or thumbnail compositions from existing channels. Use only assets whose licenses allow your intended use, including commercial use if you plan to monetize. Before publishing, review YouTube's current audience-setting, child-safety, and monetization requirements yourself.

## Reference approach

The supplied screenshots show recognizable channel patterns: colorful preschool imagery, a clear mascot/avatar, neatly grouped playlists, and a mix of full songs and Shorts. This kit uses those broad presentation ideas while defining a separate cast, setting, name, and visual identity. The screenshots and reference channel artwork are not included in this repository.

## License

The original text and scripts in this repository are released under the MIT License. This does not grant rights to any third-party assets you add later.
