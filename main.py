from discord.ext import commands
import config


class CogExample(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_extensions = (
            'cogs.admin',
            'cogs.events',
            'cogs.example',
            'cogs.routes',
        )

        for extension in self.initial_extensions:
            self.load_extension(extension)


bot = CogExample(command_prefix='ce:')
bot.run(config.token)
