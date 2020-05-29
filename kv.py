import click
import time
import os
import shutil

from modules.structures import simple_app_mvc, show_case_mvc

def colorizer(text_no_decorate, text_to_decorate, color):
    click.echo(
        text_no_decorate + click.style(
        (str(text_to_decorate)), 
        fg = color
    ))

@click.group()
def main():
    pass

@main.command('create')
@click.argument('name', 
                default = 'my_first_app', nargs = 1)
@click.option('--mode', '-m', 
              default = 'simple_app', nargs = 1, required=False)
@click.option("--arch", "-a",
              default = "mvc", required=False)
@click.option('--path', '-p',
              default = ".", nargs = 1, required=False)
def create(name, mode, arch, path):
    """create structure app."""
    app_path = path + '\\' + name
    
    if mode == 'simple_app' and arch == 'mvc':
        simple_app_mvc(app_path, name)
    elif mode == "show_case" and arch == 'mvc':
        show_case_mvc(app_path)

    colorizer("[mode] ", mode, 'green')
    colorizer("[arch] ", arch, 'green')
     
    with click.progressbar(
        iterable = [1,1], label = '[create]',
        bar_template='%(label)s %(bar)s | %(info)s',
        fill_char=click.style(u'█', fg='cyan'),
        empty_char=' ') as bar:
        for x in bar:
            time.sleep(x)
    colorizer("[status] ", f'{name} created', 'green')

@main.command('run')
@click.argument("app_name", 
                default = 'main', nargs = 1)
def run(app_name):
    os.system(f"py {app_name}.py")

@main.command('init')
def init():
    from pyfiglet import Figlet
    f = Figlet(font = 'slant')
    click.echo(click.style(f.renderText("Kivy CLI"), fg = 'blue'))
    colorizer('', "Welcome to Kivy CLI", 'green')
    colorizer('', "In Here Everything OK!!!", 'yellow')

if __name__ == "__main__":
    main()