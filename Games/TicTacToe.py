import discord 
 
class TicTacToe():
    def __init__(self):
        self.feld = [['1','2','3'],['4','5','6'],['7','8','9']]
        self.anzahlZuege = 0
        
    async def restart(self, message):
        self.feld = [['1','2','3'],['4','5','6'],['7','8','9']]
        self.anzahlZuege = 0
        embed = discord.Embed(title="TicTacTo",color=0x22a7f0)
        embed.add_field(name="Neustart", value="Neustart")
        await message.channel.send(embed=embed)

    async def next_turn(self, message):
        args = message.content.split(' ')
        if len(args) == 2:
            if(self.Result(self.feld) == False):
                self.SpielfeldChange(self.feld, int(args[1]), self.anzahlZuege)
                self.anzahlZuege+=1
                embed = discord.Embed(title="TicTacTo",color=0x22a7f0)
                embed.add_field(name="Feld:",value=self.Spielfeld(self.feld))
                await message.channel.send(embed=embed)
                if(self.Result(self.feld) == True):
                    gewonnenMessage = await message.channel.send("Hast Gewonnen {0}".format(self.Spieler(self.anzahlZuege-1)))
                    await gewonnenMessage.add_reaction("<:GayAlex:642807888280027147>") 
                    await message.channel.send("zum Neustarten !start TicTacTo schreiben")
                if(self.Unentschieden(self.feld) == True):
                    await message.channel.send("Unentschieden")
                    await message.channel.send("zum Neustarten !start TicTacTo schreiben") 

    def Spielfeld(self):
        spielfeld = ("{0} {1} {2} \n{3} {4} {5}\n{6} {7} {8}".format(
            self.feld[0][0],
            self.feld[0][1],
            self.feld[0][2],
            self.feld[1][0],
            self.feld[1][1],
            self.feld[1][2],
            self.feld[2][0],
            self.feld[2][1],
            self.feld[2][2])
        )
        return spielfeld

    def SpielfeldChange(self, spielfeld, eingabefeld):
        raus = False
        for i in range(len(spielfeld)):
            if(raus == True):
                break
            for j in range(len(spielfeld[i])):
                eingabefeld-=1
                if(eingabefeld == 0):
                    if(spielfeld[i][j] != 'X' and spielfeld[i][j] != 'O'):
                        spielfeld[i][j] = self.Spieler(self.anzahlZuege)
                        raus = True
                        break

    def GleicheZeichen(eins, zwei, drei):
        alleGleich = False
        if(eins == 'X'):
            if(zwei == 'X'):
                if(drei == 'X'):
                    alleGleich = True
        elif(eins == 'O'):
            if(zwei == 'O'):
                if(drei == 'O'):
                    alleGleich = True
        return alleGleich    

    def Unentschieden(self):
        unentschieden = False
        belegt = 0
        for i in range(len(self.feld)):
            for j in range(len(self.feld[i])):
                if(self.feld[i][j] == 'X' or self.feld[i][j] == 'O'):
                    belegt+=1
                    if(belegt == 9):
                        unentschieden = True
        return unentschieden

    def Result(self):
        Gewonnen = False
        for i in range(3):
            if(self.GleicheZeichen(self.feld[i][0],self.feld[i][1],self.feld[i][2]) == True):
                Gewonnen = True
                break
            elif(self.GleicheZeichen(self.feld[0][i],self.feld[1][i],self.feld[2][i]) == True):
                Gewonnen = True
                break
        if(self.GleicheZeichen(self.feld[0][0],self.feld[1][1],self.feld[2][2]) == True):
            Gewonnen = True      
        elif(self.GleicheZeichen(self.feld[0][2],self.feld[1][1],self.feld[2][0]) == True):
            Gewonnen = True
        return Gewonnen

    def Spieler(self):
        XO = 'X'
        if(self.anzahlZuege == 0 or self.anzahlZuege == 2 or self.anzahlZuege == 4 or self.anzahlZuege == 6 or self.anzahlZuege == 8):
            XO = 'X'    
        elif(self.anzahlZuege == 1 or self.anzahlZuege == 3 or self.anzahlZuege == 5 or self.anzahlZuege == 7 or self.anzahlZuege == 9):
            XO = 'O'
        return XO