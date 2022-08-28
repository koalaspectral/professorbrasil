import discord
import mysql.connector
from discord.ext import commands, tasks
from random import choice
from decouple import config

host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class Spawn(commands.Cog):
    '''work with spawn'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="spawnar", help="Mostra todos os seus bagmons no RP/RPG")
    @commands.has_permissions(administrator=True)
    async def spawnar(self, ctx, message):
        await ctx.message.channel.purge(limit=1)
        grupo = ['1000822505214320670','1004886201083375716']
        id = choice(grupo)
        random = ['Voara','Azurara','Ararazul','Pequemico','Douraleao','Micorado','Capi','Capilorde','Varacapi','Tamandui','Tamirim','Caralata','Caramelo','Viramelo','Astracaré','Açaíne','Bansquito','Beboto','Bodutor','Besercules','Besarela','Benja','Benjamais','Benjamuitos','Bojarro','Cafasma','Caquilete','Chanin','Colote','Diquejos','Duraiba','Duratista','Dutrino','Durito','Filho','Grafé','Iaça','Jacarevac','Jondi','Julicac','Laguito','Lutandua','Naná','Orcantos','Pamonhana','Pfizegator','Pondi','Pormeiras','Guaranin','Slicural','Torrafé','Zegoti','Jacarevac','Astracaré','Colote','Cajaça','Véiguerrero','Cuscute','Monstruz','Querokero','Biscolacha','Bolachoito','Ratinrrato','Ratobum','Querokero','Querocaos','Bentevi','Benteverei','Bentevejo','Pregaiana','Largata','Casuleta','Borboleto','Brabuleta','Uvisier','Sansoelho','Coxita','Pasfeira','Caldicana','Pequitixa','Calanqui','Peteiú','Bezeta','Carapreta','Bezela','Vacarela','Capritidos','Sapoeira','Jiusapo','Capagaz','Carcego','Morganca','Bebolvo','Octeddy','Tazum','Montazo','Fantazo','Feijote','Banloira','Mamuna','Mantrio','Massinas','Jubará','Josoré','Fixuxo','Txucão','Chifíbio','Saparrão','Chimarrã','Terereca','Sin','Salabin','Ziriguidum','Elecbol','Brazorb','Doncorvo','Canarin','Pistolin','Tatuleco','Tatunastra','Tupin','Volpiniquin','Floriniquin','Hidroniquin','Brasaniquin','Titaniquin','Urumengo','Cebrutius','Diguidin','Santaulo','Mosquião','Peixuanã','Pirarupeixe','Imperátilus','Irritator','Celeconda','Suculeste','Ursocotom','Araupinha','Araubroto','Arauforte','Xunave','Cristaluna']
        bagmon = message
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'UPDATE spawn SET bagmon = "{bagmon}" WHERE id = 1')
        if bagmon == 'Voara':
            
            image = 'https://dc341.4shared.com/img/0f7jZpa_ea/s24/18266939fd8/Voara?async&rand=0.9737188501310448'
            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')

            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Azurara':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/UHDdIK-kea/s24/18266921d20/Azurara?async&rand=0.8257013094667378'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Ararazul':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/mHJkcAWIea/s24/18266920d80/Ararazul?async&rand=0.26541024602488617'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pequemico':
            spawn = 'Pequemico'
            image = 'https://dc722.4shared.com/img/yxwZPMQSea/s24/18266932e90/Pequemico?async&rand=0.2657809932631312'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Douraleao':
            spawn = 'Douraleao'
            image = 'https://dc722.4shared.com/img/k-Fqg1Xtiq/s24/1826692ada8/Douraleao?async&rand=0.28952928296622615'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Micorado':
            spawn = 'Micorado'
            image = 'https://dc341.4shared.com/img/7g3C2-0Viq/s24/18266930b68/Micorado?async&rand=0.4206547670306653'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Capi':
            spawn = 'Capi'
            image = 'https://dc722.4shared.com/img/xWD9KeDlea/s24/18266926f28/Capi?async&rand=0.7027390789034016'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Varacapi':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/4h13tUlNiq/s24/18266939420/Varacapi?async&rand=0.9991363839552507'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Capilorde':
            spawn = 'Capilorde'
            image = 'https://dc612.4shared.com/img/nLifrdV2ea/s24/18266927310/Capilorde?async&rand=0.2132639461270145'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Tamandui':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/-AvIzwMOiq/s24/18266936d10/Tamandui?async&rand=0.5447240329519589'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Tamirim':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/KUqyo1Zvea/s24/18266936d10/Tamirim?async&rand=0.07246574676650774'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Lutandua':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/-a_q18Hpiq/s24/1826692ffb0/Lutandua?async&rand=0.8260165418034344'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Caralata':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/B-kq3Zbaiq/s24/18266927ae0/Caralata?async&rand=0.2535460832935694'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Caramelo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/F6Ym29WFiq/s24/18266927ae0/Caramelo?async&rand=0.7377648044676026'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Viramelo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/1RmUmqzfiq/s24/18266939bf0/Viramelo?async&rand=0.29435495031468273'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Astracaré':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/AWwW225Vea/s24/18266921938/Astracar?async&rand=0.1636733049801533'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Açaíne':
            spawn = 'Açaíne'
            image = 'https://dc722.4shared.com/img/jpx39MRXiq/s24/182669205b0/Aane?async&rand=0.45861453480053527'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bansquito':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/b2ZbhooKiq/s24/18266922108/Bansquito?async&rand=0.3957743690689821'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Beboto':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/94HPOjyCea/s24/182669224f0/Beboto?async&rand=0.4872536498902724'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bodutor':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/868wxCdiiq/s24/18266924c00/Bodutor?async&rand=0.7832281431613599'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Besercules':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/GxoXUa6niq/s24/18266923c60/Besercules?async&rand=0.5507626948072792'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Besarela':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/VjWyl9dvea/s24/18266923878/Besarela?async&rand=0.43207088743207955'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Benja':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/KtypoNX1ea/s24/182669228d8/Benja?async&rand=0.34817431954766853'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Benjamais':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/N3El3Kaqiq/s24/182669228d8/Benjamais?async&rand=0.7996001137359019'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Benjamuitos':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/NfyOl3h1iq/s24/18266922cc0/Benjamuitos?async&rand=0.3753855179719281'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bojarro':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/CYol1GGpea/s24/18266924fe8/Bojarro?async&rand=0.6026542286922265'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Cafasma':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/1v8RoS4fiq/s24/18266925f88/Cafasma?async&rand=0.7521426300429299'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Caquilete':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/qXpbebEtiq/s24/182669276f8/Caquilete?async&rand=0.25629047409983574'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Chanin':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/zAY2UD7Diq/s24/18266928e68/Chanin?async&rand=0.6133694483455459'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Colote':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/NrkERtf9iq/s24/18266929a20/Colote?async&rand=0.48987569799457154'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Diquejos':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/cEkvUdZ9ea/s24/1826692a5d8/Diquejos?async&rand=0.9482229786520224'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Duraiba':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/zaWXhnkuiq/s24/1826692ada8/Duraiba?async&rand=0.4102278537588997'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Duratista':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/RkErPeImea/s24/1826692b190/Duratista?async&rand=0.7584182961176469'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Dutrino':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/WvN78QCXiq/s24/1826692b578/Dutrino?async&rand=0.8386907726333865'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Durito':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/Nq6RRVi9iq/s24/1826692b578/Durito?async&rand=0.04453726125504587'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Fofilho':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/uXNHdlgZea/s24/1826692c900/Fofilho?async&rand=0.45051158395091395'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Grafé':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/O4KnukrNiq/s24/1826692cce8/Graf?async&rand=0.867112443484868'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Iaça':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/d2eCtYeNea/s24/1826692d4b8/Iaa?async&rand=0.8655287434112704'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Jacarevac':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/0vZk7DaHiq/s24/1826692e070/Jacarevac?async&rand=0.8297306931732571'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Jondi':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/RcSngiXdiq/s24/1826692e840/Jondi?async&rand=0.7833560200730421'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Julicac':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/p-Z7fUSJiq/s24/1826692f010/Julicac?async&rand=0.6947279390067365'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Laguito':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/oxqel1oviq/s24/1826692f3f8/Laguito?async&rand=0.36172362990670415'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Naná':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/0U5aG_D6ea/s24/18266931b08/Nan?async&rand=0.5950208203280252'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Orcantos':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/q4prdbctiq/s24/182669322d8/Orcantos?async&rand=0.2284164081668143'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pamonhana':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/vH6DSpv9iq/s24/182669326c0/Pamonhana?async&rand=0.820073245490383'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pfizegator':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/pyg2Qs7Sea/s24/18266933660/Pfizegator?async&rand=0.7886996114168898'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pondi':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/0-nqJWbliq/s24/18266933e30/Pondi?async&rand=0.9414058660799287'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pormeiras':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/DvB25xRaiq/s24/18266934218/Pormeiras?async&rand=0.26177046772093115'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Guaranin':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/LlM5OkCSea/s24/1826692d0d0/Guaranin?async&rand=0.11889780148445639'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Slicural':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/UqiehZo0iq/s24/18266936540/Slicurau?async&rand=0.8041149475325269'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Torrafé':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/WxsrOfsCiq/s24/18266938098/Torraf?async&rand=0.2230217319626091'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Zegoti':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/TSkSTZO9iq/s24/1826693a7a8/Zegoti?async&rand=0.02660027044052171'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Cajaça':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/PRkeZZo_iq/s24/18266926370/Cajaa?async&rand=0.7952136940472962'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Véiguerrero':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/HJtV6L5Gea/s24/18266939808/Viguerrero?async&rand=0.0712272099818525'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Cuscute':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/IaHdxPoyea/s24/1826692a1f0/Cuscute?async&rand=0.44599284530504857'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Monstruz':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/InKciAEKiq/s24/18266930f50/Monstruz?async&rand=0.5860771893367751'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Querokero':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/rIh78ICXiq/s24/182669349e8/Querokero?async&rand=0.6476364320518428'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Biscolacha':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/hSyVuNz3ea/s24/18266924818/Biscolacha?async&rand=0.3196385411770861'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bolachoito':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/eeVH6i2qiq/s24/18266924fe8/Bolachoito?async&rand=0.574101895207273'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Ratinrrato':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/EN0lnUGLea/s24/18266934dd0/Ratinrrato?async&rand=0.9737638435794522'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Ratobum':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/SyXDAn1yiq/s24/182669351b8/Ratobum?async&rand=0.6441597903115022'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Querocaos':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/TmWJhTguea/s24/182669349e8/Querocaos?async&rand=0.46720537608570023'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bentevi':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/VwqTof5vea/s24/18266923878/Bentevi?async&rand=0.7320020366317728'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Benteverei':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/21aJwH2xiq/s24/18266923490/Benteverei?async&rand=0.5954871142847595'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bentevejo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/G_HcPzUCiq/s24/182669230a8/Bentevejo?async&rand=0.0036284533676476105'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pregaiana':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/mwa_jHTuea/s24/18266934600/Pregaiana?async&rand=0.9609247772094225'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Largata':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/HKVr_icsiq/s24/1826692fbc8/Largata?async&rand=0.048085198300005905'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Casuleta':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/-JHzGjuAiq/s24/18266928698/Casuleta?async&rand=0.5208893629260793'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Borboleto':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/VRaztbexea/s24/182669253d0/Borboleto?async&rand=0.5004776160359565'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Brabuleta':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/iNkmYZW-iq/s24/182669253d0/Brabuleta?async&rand=0.738445840742959'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Uvisier':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/LVw-TwTTiq/s24/18266938c50/Uvisier?async&rand=0.5536656537672138'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Sansoelho':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/M4buIXYAiq/s24/18266935988/Sansoelho?async&rand=0.6677248568893375'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Coxita':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/voBM6x3aiq/s24/18266929a20/Coxita?async&rand=0.795640049798946'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pasfeira':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/CMfTDcPPea/s24/182669326c0/Pasfeira?async&rand=0.1758728951960713'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Caldicana':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/BoDNBKhjiq/s24/18266926758/Caldicana?async&rand=0.8430706589788342'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pequitixa':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/10HgHzVAiq/s24/18266932e90/Pequitixa?async&rand=0.3235294165848708'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Calanqui':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/Hg4Sj_O0ea/s24/18266926758/Calanqui?async&rand=0.5178007770325603'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Peteiú':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/iriiiZF0ea/s24/18266933278/Petei?async&rand=0.2716261533708022'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bezeta':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/VllV7Jjbea/s24/18266924048/Bezeta?async&rand=0.7350289415987938'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Carapreta':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/36pngbXtea/s24/182669282b0/Carapreta?async&rand=0.3760354055373729'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bezela':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/ct-MTCNnea/s24/18266924048/Bezela?async&rand=0.5946040723164556'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Vacarela':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/ibBtYNY-iq/s24/18266939038/Vacarela?async&rand=0.7713539153119944'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Capritidos':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/nQ4ssFY2iq/s24/182669276f8/Capritidos?async&rand=0.6976237049001808'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Sapoeira':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/g7WYrDQwea/s24/18266935d70/Sapoeira?async&rand=0.7540577683114225'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Saparrão':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/5IDZBKkjea/s24/18266935d70/Saparro?async&rand=0.5664804488795494'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Jiusapo':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/VZKIsA2Miq/s24/1826692e458/Jiusapo?async&rand=0.5596963328061291'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Capagaz':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/9Y0PuoyNiq/s24/18266926f28/Capagaz?async&rand=0.5735835805506047'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Carcego':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/876C2_0_ea/s24/182669282b0/Carcego?async&rand=0.2825895048633471'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Morganca':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/7MBr-hYbiq/s24/18266931338/Morganca?async&rand=0.14374952381973372'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bebolvo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/FeWLlnhvea/s24/18266922108/Bebolvo?async&rand=0.7675302191695683'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Octeddy':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/Fg-4M87lea/s24/18266931ef0/Octeddy?async&rand=0.09111683725891262'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Tazum':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/MEAoQxX8ea/s24/182669374e0/Tazum?async&rand=0.9597196902922065'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Montazo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/MoAqO3r8iq/s24/18266930f50/Montazo?async&rand=0.832187972895243'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Fantazo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/zEKao69Liq/s24/1826692bd48/Fantazo?async&rand=0.052947235137780435'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Feijote':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/u4sB1LKFea/s24/1826692bd48/Feijote?async&rand=0.8477299912383576'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Banloira':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/WQ4qu_r3iq/s24/18266921d20/Banloira?async&rand=0.5085280264771983'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Mamuna':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/C8Bee0Ediq/s24/1826692ffb0/Mamuna?async&rand=0.3431105181101517'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Mantrio':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/xYNFbRLYea/s24/18266930398/Mantrio?async&rand=0.48345649213349184'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Massinas':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/RtmSjWOeiq/s24/18266930780/Massinas?async&rand=0.7119373638194209'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Jubará':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/zpNt5QIWiq/s24/1826692ec28/Jubar?async&rand=0.31667770515304716'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Josoré':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/C-PhLRV7ea/s24/1826692ec28/Joser?async&rand=0.7191686629540419'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Fixuxo':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/VD8Tom5fiq/s24/1826692c130/Fixuxo?async&rand=0.3053668265452625'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Txucão':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/oX1HFogQea/s24/18266938480/Txuco?async&rand=0.6219801264396032'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Chifíbio':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/YEq7pLmwea/s24/18266929250/Chifbio?async&rand=0.17610309541909297'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Chimarrã':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/add74HCGea/s24/18266929250/Chimarr?async&rand=0.52323165064816'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Terereca':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/Er63NVl8ea/s24/182669378c8/Terereca?async&rand=0.26694862371445005'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Sin':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/GdOZdRkZiq/s24/18266936540/Sin?async&rand=0.8111151569243265'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Salabin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/khqaf1Ttiq/s24/182669355a0/Salabin?async&rand=0.7203894991541768'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Ziriguidum':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/Nj-2KCBliq/s24/1826693ab90/Ziriguidum?async&rand=0.5577703642599972'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Elecbol':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/5AulnMGLea/s24/1826692b960/Electobol?async&rand=0.2600633647550026'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Brazorb':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/ltZe99UHea/s24/18266925f88/Brazorb?async&rand=0.9990035088223967'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Doncorvo':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/S4V7fPStea/s24/1826692a9c0/Doncorvo?async&rand=0.673837902017733'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Canarin':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/yFBZ_Nkcea/s24/18266926b40/Canarin?async&rand=0.5428991139172854'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pistolin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/tTb8FXmAiq/s24/18266933e30/Pistolin?async&rand=0.3946697531986816'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Tatuleco':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/3YYzVneEiq/s24/182669370f8/Tatuleco?async&rand=0.36545464603152866'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Tatunastra':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/3TWgoD_viq/s24/182669374e0/Tatunastra?async&rand=0.9284501833276133'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Tupin':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/A6A4X3R-iq/s24/18266938480/Tupin?async&rand=0.8155121161147894'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Volpiniquin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/ZRpL8axrea/s24/1826693a3c0/Volpiniquin?async&rand=0.2639444307679739'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Floriniquin':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/RymAnqKfea/s24/1826692c518/Floriniquin?async&rand=0.18256994783039393'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Hidroniquin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/wundBGojiq/s24/1826692d0d0/Hidroniquin?async&rand=0.5809724736936892'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Brasaniquin':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/LtjoDtH5ea/s24/18266925ba0/Brasaniquin?async&rand=0.5694876522109928'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Titaniquin':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/Shzwuxt3ea/s24/18266937cb0/Titaniquin?async&rand=0.6241598344316126'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Urumengo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/fmYjLnGBea/s24/18266938c50/Urumengo?async&rand=0.8407953024936519'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Cebrutius':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/cWQw0Bt_iq/s24/18266928a80/Cebrutius?async&rand=0.14187859434702688'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Diguidin':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/ThWZiTAuea/s24/1826692a1f0/Diguidim?async&rand=0.3662429675599945'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Santaulo':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/d9EzYe0oea/s24/18266935988/Santaulo?async&rand=0.34017637630805053'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Mosquião':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/TkkjNda8iq/s24/18266931720/Mosquio?async&rand=0.7181766359655479'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Peixuanã':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/P6gRYI4Uiq/s24/18266932aa8/Peixuan?async&rand=0.3943120949107679'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Pirarupeixe':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/hoMpNQbSea/s24/18266933660/Pirarupeixe?async&rand=0.9303702573770767'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Imperátilus':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/CYhBcJ0Yiq/s24/1826692d8a0/Impertilus?async&rand=0.164407415069727'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Irritator':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/CvjiBZp5iq/s24/1826692dc88/Irritator?async&rand=0.4752632376058299'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Celeconda':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/hRrfIf_Aiq/s24/18266928a80/Celeconda?async&rand=0.3978117429024588'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Suculeste':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/mJmOlWhfea/s24/18266936928/Suculeste?async&rand=0.15537812082329583'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Ursocotom':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/CGwsRwcTea/s24/18266938868/Ursocotom?async&rand=0.48217215601645824'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Araupinha':
            spawn = 'Araupinha'
            image = 'https://dc612.4shared.com/img/Dgavlbdviq/s24/18266921550/Araupinha?async&rand=0.374921704299225'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Araubroto':
            spawn = 'Araubroto'
            image = 'https://dc612.4shared.com/img/XdUXQi6miq/s24/18266921168/Araubroto?async&rand=0.6258116852881619'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Arauforte':
            spawn = 'Arauforte'
            image = 'https://dc612.4shared.com/img/XY2E2E1Viq/s24/18266921168/Arauforte?async&rand=0.20453222165198337'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Xunave':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/37jIGtw6iq/s24/1826693a3c0/Xunave?async&rand=0.47099571618307756'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Cristaluna':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/6Vw9Yg9Uea/s24/18266929e08/Cristaluna?async&rand=0.6246534777719688'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bilu':
            spawn = 'Azurara'
            image = 'https://dc612.4shared.com/img/6mE_SKDnea/s24/18266924430/Bilu?async&rand=0.5060401733915738'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Loguará':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/--E10eBpiq/s24/1826692fbc8/Loguar?async&rand=0.15519064265412097'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Sereiara':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/p8HcIz-Aea/s24/18266936158/Sereiara?async&rand=0.08812573855256578'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Piropira':
            spawn = 'Azurara'
            image = 'https://dc722.4shared.com/img/Wp5MxFh4iq/s24/18266933a48/Piropira?async&rand=0.32225447415088326'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Sacerê':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/S0tCb2KIea/s24/182669351b8/Sacer?async&rand=0.004201455384246877'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Mapinguá':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/nfVj2iWpiq/s24/18266930780/Mapingu?async&rand=0.7292781577638543'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Gambiarros':
            spawn = 'Azurara'
            image = 'https://dc341.4shared.com/img/8-e4vYRNiq/s24/1826692c900/Gambiarros?async&rand=0.8123111213134038'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Velopya':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/xSs5TfSDiq/s24/18266939bf0/Velopya?async&rand=0.07768439603123212'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Mulantã':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/H5MXZkkVea/s24/18266931720/Mulant?async&rand=0.8791841275322927'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Cobratá':
            spawn = 'Ararazul'
            image = 'https://dc612.4shared.com/img/exm4mWBfea/s24/18266929638/Cobrat?async&rand=0.7905911665947039'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)  
        elif bagmon == 'Iaguará':
            spawn = 'Ararazul'
            image = 'https://dc341.4shared.com/img/ij_j4mqqea/s24/1826692d8a0/Iaguar?async&rand=0.6757360574938176'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        elif bagmon == 'Bivaldo':
            spawn = 'Ararazul'
            image = 'https://dc722.4shared.com/img/py0TpojMea/s24/18266924818/Bivaldo?async&rand=0.27840931299886407'

            cursor.execute(f'UPDATE spawn SET url = ("{image}") WHERE id = 1')
            db.commit()
            spawnb = discord.Embed(
                title = '**Um bagmon apareceu**',
                color = 0xff000f,
            )
            spawnb.set_image(url=image)
            spawnb.set_footer(text='Digite b!catch <bagmon> para capturalo')
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
            
        else:
            spawnb = discord.Embed(
                title = '**Me parece que este bagmon ainda nao foi descoberto, rsrs**',
                color = 0xff000f,
            )
            channel = self.bot.get_channel(1004886201083375716)
            await ctx.send(embed=spawnb)
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(Spawn(bot))

    
