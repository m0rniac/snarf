# [Corpus; Async Libs].
import os
import sys
import os.path
import click
import asyncio

# [Corpus; Snarf Components].
from . import SNARF, snarf_dir, SNARFError


# [Corpus; INIT].
async def a_main(voice_name, text, filename, rate, pitch, volume):
    snarfy = SNARF()
    
    v = await snarfy.get_voices_by_substring(voice_name)
    
    if len(v) == 0:
        raise SNARFError("The voice was not found.")
    
    await snarfy.set_voice(v[0]['Name'])
    await snarfy.set_rate(rate)
    await snarfy.set_pitch(pitch)
    await snarfy.set_volume(volume)
    await snarfy.synthesize(text.strip(), filename)


# [Corpus; Promt commands].
@click.command(context_settings = {'help_option_names': ['-h', '--help']})
@click.argument("voice_name")
@click.argument("text")
@click.option("--filename", default = "snarf_audio.mp3", help = "Audio file name.")
@click.option("--rate", default = 0, help = "Speech rate (from 1 to 20, or 0).")
@click.option("--pitch", default = 0, help = "voice pitch (from 1 to 20, or 0).")
@click.option("--volume", default = 1.0, help = "voice volume.")


# [Corpus; Main Function].
def main(voice_name, text, filename = "snarf_audio.mp3", rate = 0, pitch = 0, volume = 1.0):
    # {subCorpus; Fetch generated tts sounds from SNARF}
    try:
        loop = asyncio.get_event_loop()
        click.echo(loop.run_until_complete(a_main(
            voice_name = voice_name,
            text = text,
            filename = filename,
            rate = rate,
            pitch = pitch,
            volume = volume
        )))
    except SNARFError as exn:
        click.secho(str(exn), fg = 'red')
        raise SystemExit(-2)


# [Corpus; Update].
@click.command()
def update_voices():
    # {subCorpus; Deleting the file with the list of voices and download the list of voices again}
    removed = False
    for f in ["voices_list.json", "voices_list_plus.json"]:
        p = os.path.join(snarf_dir, f)
        if os.path.isfile(p):
            removed = True
            click.echo(f"removing {p}")
            os.remove(p)
    if not removed:
        click.echo("Files not found")
    snarfy = SNARF()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(snarfy.get_voices_list())



# [Corpus; Execution].
if __name__ == '__main__':
    if sys.argv[-1].replace("-", "_").lower() == "update_voices":
        update_voices()
        sys.exit(0)
    main()