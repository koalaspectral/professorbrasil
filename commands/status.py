from discord.ext import commands
import discord
import mysql.connector
from decouple import config

host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class status(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='status')
    async def pick(self, ctx, message):
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM capturas WHERE user = {ctx.author.id} AND bagmon = "{message}"')
        bagmon = cursor.fetchone()
        if message == 'Voara':
            
            image = 'https://dc341.4shared.com/img/0f7jZpa_ea/s24/18266939fd8/Voara?async&rand=0.9737188501310448'
            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)


            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Azurara':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/UHDdIK-kea/s24/18266921d20/Azurara?async&rand=0.8257013094667378'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Ararazul':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/mHJkcAWIea/s24/18266920d80/Ararazul?async&rand=0.26541024602488617'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pequemico':
            spawn = 'Pequemico'
            image = 'https://dc722.4shared.com/img/yxwZPMQSea/s24/18266932e90/Pequemico?async&rand=0.2657809932631312'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Douraleao':
            spawn = 'Douraleao'
            image = 'https://dc722.4shared.com/img/k-Fqg1Xtiq/s24/1826692ada8/Douraleao?async&rand=0.28952928296622615'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Micorado':
            spawn = 'Micorado'
            image = 'https://dc341.4shared.com/img/7g3C2-0Viq/s24/18266930b68/Micorado?async&rand=0.4206547670306653'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Capi':
            spawn = 'Capi'
            image = 'https://dc722.4shared.com/img/xWD9KeDlea/s24/18266926f28/Capi?async&rand=0.7027390789034016'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Varacapi':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/mHJkcAWIea/s24/18266920d80/Ararazul?async&rand=0.26541024602488617'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Capilorde':
            spawn = 'Capilorde'
            image = 'https://dc612.4shared.com/img/nLifrdV2ea/s24/18266927310/Capilorde?async&rand=0.2132639461270145'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Tamandui':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/-AvIzwMOiq/s24/18266936d10/Tamandui?async&rand=0.5447240329519589'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Tamirim':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/KUqyo1Zvea/s24/18266936d10/Tamirim?async&rand=0.07246574676650774'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Lutandua':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/-a_q18Hpiq/s24/1826692ffb0/Lutandua?async&rand=0.8260165418034344'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Caralata':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/B-kq3Zbaiq/s24/18266927ae0/Caralata?async&rand=0.2535460832935694'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Caramelo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/F6Ym29WFiq/s24/18266927ae0/Caramelo?async&rand=0.7377648044676026'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Viramelo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/1RmUmqzfiq/s24/18266939bf0/Viramelo?async&rand=0.29435495031468273'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Astracaré':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/AWwW225Vea/s24/18266921938/Astracar?async&rand=0.1636733049801533'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Açaíne':
            spawn = 'Açaíne'
            image = 'https://dc722.4shared.com/img/jpx39MRXiq/s24/182669205b0/Aane?async&rand=0.45861453480053527'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bansquito':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/b2ZbhooKiq/s24/18266922108/Bansquito?async&rand=0.3957743690689821'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Beboto':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/94HPOjyCea/s24/182669224f0/Beboto?async&rand=0.4872536498902724'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bodutor':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/868wxCdiiq/s24/18266924c00/Bodutor?async&rand=0.7832281431613599'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Besercules':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/GxoXUa6niq/s24/18266923c60/Besercules?async&rand=0.5507626948072792'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Besarela':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/VjWyl9dvea/s24/18266923878/Besarela?async&rand=0.43207088743207955'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Benja':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/KtypoNX1ea/s24/182669228d8/Benja?async&rand=0.34817431954766853'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Benjamais':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/N3El3Kaqiq/s24/182669228d8/Benjamais?async&rand=0.7996001137359019'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Benjamuitos':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/NfyOl3h1iq/s24/18266922cc0/Benjamuitos?async&rand=0.3753855179719281'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bojarro':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/CYol1GGpea/s24/18266924fe8/Bojarro?async&rand=0.6026542286922265'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Cafasma':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/1v8RoS4fiq/s24/18266925f88/Cafasma?async&rand=0.7521426300429299'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Caquilete':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/qXpbebEtiq/s24/182669276f8/Caquilete?async&rand=0.25629047409983574'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Chanin':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/zAY2UD7Diq/s24/18266928e68/Chanin?async&rand=0.6133694483455459'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Colote':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/NrkERtf9iq/s24/18266929a20/Colote?async&rand=0.48987569799457154'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Diquejos':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/cEkvUdZ9ea/s24/1826692a5d8/Diquejos?async&rand=0.9482229786520224'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Duraiba':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/zaWXhnkuiq/s24/1826692ada8/Duraiba?async&rand=0.4102278537588997'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Duratista':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/RkErPeImea/s24/1826692b190/Duratista?async&rand=0.7584182961176469'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Dutrino':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/WvN78QCXiq/s24/1826692b578/Dutrino?async&rand=0.8386907726333865'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Durito':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/Nq6RRVi9iq/s24/1826692b578/Durito?async&rand=0.04453726125504587'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Fofilho':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/uXNHdlgZea/s24/1826692c900/Fofilho?async&rand=0.45051158395091395'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Grafé':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/O4KnukrNiq/s24/1826692cce8/Graf?async&rand=0.867112443484868'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Iaça':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/d2eCtYeNea/s24/1826692d4b8/Iaa?async&rand=0.8655287434112704'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Jacarevac':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/0vZk7DaHiq/s24/1826692e070/Jacarevac?async&rand=0.8297306931732571'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Jondi':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/RcSngiXdiq/s24/1826692e840/Jondi?async&rand=0.7833560200730421'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Julicac':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/p-Z7fUSJiq/s24/1826692f010/Julicac?async&rand=0.6947279390067365'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Laguito':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/oxqel1oviq/s24/1826692f3f8/Laguito?async&rand=0.36172362990670415'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Naná':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/0U5aG_D6ea/s24/18266931b08/Nan?async&rand=0.5950208203280252'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Orcantos':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/q4prdbctiq/s24/182669322d8/Orcantos?async&rand=0.2284164081668143'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pamonhana':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/vH6DSpv9iq/s24/182669326c0/Pamonhana?async&rand=0.820073245490383'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pfizegator':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/pyg2Qs7Sea/s24/18266933660/Pfizegator?async&rand=0.7886996114168898'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pondi':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/0-nqJWbliq/s24/18266933e30/Pondi?async&rand=0.9414058660799287'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pormeiras':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/DvB25xRaiq/s24/18266934218/Pormeiras?async&rand=0.26177046772093115'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Guaranin':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/LlM5OkCSea/s24/1826692d0d0/Guaranin?async&rand=0.11889780148445639'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Slicural':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/UqiehZo0iq/s24/18266936540/Slicurau?async&rand=0.8041149475325269'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Torrafé':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/WxsrOfsCiq/s24/18266938098/Torraf?async&rand=0.2230217319626091'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Zegoti':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/TSkSTZO9iq/s24/1826693a7a8/Zegoti?async&rand=0.02660027044052171'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Cajaça':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/PRkeZZo_iq/s24/18266926370/Cajaa?async&rand=0.7952136940472962'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Véiguerrero':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/HJtV6L5Gea/s24/18266939808/Viguerrero?async&rand=0.0712272099818525'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Cuscute':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/IaHdxPoyea/s24/1826692a1f0/Cuscute?async&rand=0.44599284530504857'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Monstruz':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/InKciAEKiq/s24/18266930f50/Monstruz?async&rand=0.5860771893367751'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Querokero':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/rIh78ICXiq/s24/182669349e8/Querokero?async&rand=0.6476364320518428'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Biscolacha':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/hSyVuNz3ea/s24/18266924818/Biscolacha?async&rand=0.3196385411770861'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bolachoito':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/eeVH6i2qiq/s24/18266924fe8/Bolachoito?async&rand=0.574101895207273'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Ratinrrato':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/EN0lnUGLea/s24/18266934dd0/Ratinrrato?async&rand=0.9737638435794522'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Ratobum':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/SyXDAn1yiq/s24/182669351b8/Ratobum?async&rand=0.6441597903115022'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Querocaos':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/TmWJhTguea/s24/182669349e8/Querocaos?async&rand=0.46720537608570023'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bentevi':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/VwqTof5vea/s24/18266923878/Bentevi?async&rand=0.7320020366317728'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Benteverei':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/21aJwH2xiq/s24/18266923490/Benteverei?async&rand=0.5954871142847595'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bentevejo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/G_HcPzUCiq/s24/182669230a8/Bentevejo?async&rand=0.0036284533676476105'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pregaiana':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/mwa_jHTuea/s24/18266934600/Pregaiana?async&rand=0.9609247772094225'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Largata':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/HKVr_icsiq/s24/1826692fbc8/Largata?async&rand=0.048085198300005905'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Casuleta':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/-JHzGjuAiq/s24/18266928698/Casuleta?async&rand=0.5208893629260793'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Borboleto':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/VRaztbexea/s24/182669253d0/Borboleto?async&rand=0.5004776160359565'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Brabuleta':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/iNkmYZW-iq/s24/182669253d0/Brabuleta?async&rand=0.738445840742959'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Uvisier':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/LVw-TwTTiq/s24/18266938c50/Uvisier?async&rand=0.5536656537672138'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Sansoelho':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/M4buIXYAiq/s24/18266935988/Sansoelho?async&rand=0.6677248568893375'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Coxita':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/voBM6x3aiq/s24/18266929a20/Coxita?async&rand=0.795640049798946'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pasfeira':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/CMfTDcPPea/s24/182669326c0/Pasfeira?async&rand=0.1758728951960713'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Caldicana':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/BoDNBKhjiq/s24/18266926758/Caldicana?async&rand=0.8430706589788342'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pequitixa':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/10HgHzVAiq/s24/18266932e90/Pequitixa?async&rand=0.3235294165848708'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Calanqui':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/Hg4Sj_O0ea/s24/18266926758/Calanqui?async&rand=0.5178007770325603'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Peteiú':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/iriiiZF0ea/s24/18266933278/Petei?async&rand=0.2716261533708022'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bezeta':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/VllV7Jjbea/s24/18266924048/Bezeta?async&rand=0.7350289415987938'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Carapreta':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/36pngbXtea/s24/182669282b0/Carapreta?async&rand=0.3760354055373729'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bezela':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/ct-MTCNnea/s24/18266924048/Bezela?async&rand=0.5946040723164556'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Vacarela':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/ibBtYNY-iq/s24/18266939038/Vacarela?async&rand=0.7713539153119944'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Capritidos':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/nQ4ssFY2iq/s24/182669276f8/Capritidos?async&rand=0.6976237049001808'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Sapoeira':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/g7WYrDQwea/s24/18266935d70/Sapoeira?async&rand=0.7540577683114225'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Saparrão':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/5IDZBKkjea/s24/18266935d70/Saparro?async&rand=0.5664804488795494'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Jiusapo':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/VZKIsA2Miq/s24/1826692e458/Jiusapo?async&rand=0.5596963328061291'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Capagaz':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/9Y0PuoyNiq/s24/18266926f28/Capagaz?async&rand=0.5735835805506047'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Carcego':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/876C2_0_ea/s24/182669282b0/Carcego?async&rand=0.2825895048633471'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Morganca':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/7MBr-hYbiq/s24/18266931338/Morganca?async&rand=0.14374952381973372'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bebolvo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/FeWLlnhvea/s24/18266922108/Bebolvo?async&rand=0.7675302191695683'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Octeddy':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/Fg-4M87lea/s24/18266931ef0/Octeddy?async&rand=0.09111683725891262'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Tazum':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/MEAoQxX8ea/s24/182669374e0/Tazum?async&rand=0.9597196902922065'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Montazo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/MoAqO3r8iq/s24/18266930f50/Montazo?async&rand=0.832187972895243'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Fantazo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/zEKao69Liq/s24/1826692bd48/Fantazo?async&rand=0.052947235137780435'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Feijote':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/u4sB1LKFea/s24/1826692bd48/Feijote?async&rand=0.8477299912383576'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Banloira':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/WQ4qu_r3iq/s24/18266921d20/Banloira?async&rand=0.5085280264771983'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Mamuna':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/C8Bee0Ediq/s24/1826692ffb0/Mamuna?async&rand=0.3431105181101517'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Mantrio':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/xYNFbRLYea/s24/18266930398/Mantrio?async&rand=0.48345649213349184'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Massinas':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/RtmSjWOeiq/s24/18266930780/Massinas?async&rand=0.7119373638194209'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Jubará':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/zpNt5QIWiq/s24/1826692ec28/Jubar?async&rand=0.31667770515304716'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Josoré':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/C-PhLRV7ea/s24/1826692ec28/Joser?async&rand=0.7191686629540419'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Fixuxo':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/VD8Tom5fiq/s24/1826692c130/Fixuxo?async&rand=0.3053668265452625'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Txucão':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/oX1HFogQea/s24/18266938480/Txuco?async&rand=0.6219801264396032'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Chifíbio':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/YEq7pLmwea/s24/18266929250/Chifbio?async&rand=0.17610309541909297'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Chimarrã':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/add74HCGea/s24/18266929250/Chimarr?async&rand=0.52323165064816'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Terereca':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/Er63NVl8ea/s24/182669378c8/Terereca?async&rand=0.26694862371445005'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Sin':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/GdOZdRkZiq/s24/18266936540/Sin?async&rand=0.8111151569243265'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Salabin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/khqaf1Ttiq/s24/182669355a0/Salabin?async&rand=0.7203894991541768'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Ziriguidum':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/Nj-2KCBliq/s24/1826693ab90/Ziriguidum?async&rand=0.5577703642599972'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Elecbol':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/5AulnMGLea/s24/1826692b960/Electobol?async&rand=0.2600633647550026'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Brazorb':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/ltZe99UHea/s24/18266925f88/Brazorb?async&rand=0.9990035088223967'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Doncorvo':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/S4V7fPStea/s24/1826692a9c0/Doncorvo?async&rand=0.673837902017733'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Canarin':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/yFBZ_Nkcea/s24/18266926b40/Canarin?async&rand=0.5428991139172854'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pistolin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/tTb8FXmAiq/s24/18266933e30/Pistolin?async&rand=0.3946697531986816'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Tatuleco':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/3YYzVneEiq/s24/182669370f8/Tatuleco?async&rand=0.36545464603152866'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Tatunastra':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/3TWgoD_viq/s24/182669374e0/Tatunastra?async&rand=0.9284501833276133'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Tupin':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/A6A4X3R-iq/s24/18266938480/Tupin?async&rand=0.8155121161147894'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Volpiniquin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/ZRpL8axrea/s24/1826693a3c0/Volpiniquin?async&rand=0.2639444307679739'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Floriniquin':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/RymAnqKfea/s24/1826692c518/Floriniquin?async&rand=0.18256994783039393'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Hidroniquin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/wundBGojiq/s24/1826692d0d0/Hidroniquin?async&rand=0.5809724736936892'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Brasaniquin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/LtjoDtH5ea/s24/18266925ba0/Brasaniquin?async&rand=0.5694876522109928'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Titaniquin':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/Shzwuxt3ea/s24/18266937cb0/Titaniquin?async&rand=0.6241598344316126'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Urumengo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/fmYjLnGBea/s24/18266938c50/Urumengo?async&rand=0.8407953024936519'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Cebrutius':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/cWQw0Bt_iq/s24/18266928a80/Cebrutius?async&rand=0.14187859434702688'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Diguidin':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/ThWZiTAuea/s24/1826692a1f0/Diguidim?async&rand=0.3662429675599945'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Santaulo':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/d9EzYe0oea/s24/18266935988/Santaulo?async&rand=0.34017637630805053'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Mosquião':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/TkkjNda8iq/s24/18266931720/Mosquio?async&rand=0.7181766359655479'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Peixuanã':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/P6gRYI4Uiq/s24/18266932aa8/Peixuan?async&rand=0.3943120949107679'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Pirarupeixe':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/hoMpNQbSea/s24/18266933660/Pirarupeixe?async&rand=0.9303702573770767'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Imperátilus':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/CYhBcJ0Yiq/s24/1826692d8a0/Impertilus?async&rand=0.164407415069727'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Irritator':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/CvjiBZp5iq/s24/1826692dc88/Irritator?async&rand=0.4752632376058299'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Celeconda':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/hRrfIf_Aiq/s24/18266928a80/Celeconda?async&rand=0.3978117429024588'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Suculeste':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/mJmOlWhfea/s24/18266936928/Suculeste?async&rand=0.15537812082329583'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Ursocotom':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/CGwsRwcTea/s24/18266938868/Ursocotom?async&rand=0.48217215601645824'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Araupinha':
            spawn = 'Araupinha'
            image = 'https://dc612.4shared.com/img/Dgavlbdviq/s24/18266921550/Araupinha?async&rand=0.374921704299225'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Araubroto':
            spawn = 'Araubroto'
            image = 'https://dc612.4shared.com/img/XdUXQi6miq/s24/18266921168/Araubroto?async&rand=0.6258116852881619'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Arauforte':
            spawn = 'Arauforte'
            image = 'https://dc612.4shared.com/img/XY2E2E1Viq/s24/18266921168/Arauforte?async&rand=0.20453222165198337'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Xunave':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/37jIGtw6iq/s24/1826693a3c0/Xunave?async&rand=0.47099571618307756'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Cristaluna':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/6Vw9Yg9Uea/s24/18266929e08/Cristaluna?async&rand=0.6246534777719688'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bilu':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/6mE_SKDnea/s24/18266924430/Bilu?async&rand=0.5060401733915738'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Loguará':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/--E10eBpiq/s24/1826692fbc8/Loguar?async&rand=0.15519064265412097'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Sereiara':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/p8HcIz-Aea/s24/18266936158/Sereiara?async&rand=0.08812573855256578'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Piropira':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/Wp5MxFh4iq/s24/18266933a48/Piropira?async&rand=0.32225447415088326'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Sacerê':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/S0tCb2KIea/s24/182669351b8/Sacer?async&rand=0.004201455384246877'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Mapinguá':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/nfVj2iWpiq/s24/18266930780/Mapingu?async&rand=0.7292781577638543'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Gambiarros':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/8-e4vYRNiq/s24/1826692c900/Gambiarros?async&rand=0.8123111213134038'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Velopya':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/xSs5TfSDiq/s24/18266939bf0/Velopya?async&rand=0.07768439603123212'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Mulantã':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/H5MXZkkVea/s24/18266931720/Mulant?async&rand=0.8791841275322927'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Cobratá':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/exm4mWBfea/s24/18266929638/Cobrat?async&rand=0.7905911665947039'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)  
        elif message == 'Iaguará':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/ij_j4mqqea/s24/1826692d8a0/Iaguar?async&rand=0.6757360574938176'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif message == 'Bivaldo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/py0TpojMea/s24/18266924818/Bivaldo?async&rand=0.27840931299886407'

            spawnb = discord.Embed(
                title = f'**Info do {bagmon[3]} de {ctx.author.name}**',
                description =  f"HP:{bagmon[6]} XP:{bagmon[4]} Level:{bagmon[5]}",
                color = 0xff000f,
            )
            spawnb.set_image(url=image)

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
            
        else:
            spawnb = discord.Embed(
                title = f'**Me parece que este bagmon ainda nao foi descoberto, rsrs**',
                color = 0xff000f,
            )
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)

    
def setup(bot):
    bot.add_cog(status(bot))

    
