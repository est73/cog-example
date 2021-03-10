from discord.ext import commands
from subprocess import Popen, PIPE, STDOUT


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, module: str):
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'{module} loaded')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, module: str):
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'{module} unloaded')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, module: str):
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'{module} reloaded')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def pull(self, ctx, repo):
        output = ''
        proc = Popen(['git', 'pull', '--progress'], stdout=PIPE, stderr=STDOUT, text=True)
        for line in proc.stdout:
            if line and any(ele in line.lower() for ele in ['cloning', 'done', 'total', 'error']):
                output += f'{line.strip()}\n'
        await ctx.send(output)


def setup(bot):
    bot.add_cog(Admin(bot))
