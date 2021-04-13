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
            if(self.Result() == False):
                self.SpielfeldChange((int)(args[1]))
                self.anzahlZuege+=1
                embed = discord.Embed(title="TicTacTo",color=0x22a7f0)
                embed.add_field(name="Feld:",value=self.Spielfeld())
                await message.channel.send(embed=embed)
                if(self.Result() == True):
                    gewonnenMessage = await message.channel.send("Hast Gewonnen {0}".format(self.Spieler()))
                    await gewonnenMessage.add_reaction("<:GayAlex:642807888280027147>") 
                    await message.channel.send("zum Neustarten !start TicTacTo schreiben")
                if(self.Unentschieden() == True):
                    await message.channel.send("Unentschieden")
                    await message.channel.send("zum Neustarten !start TicTacTo schreiben") 

    def Spielfeld(self):
        spielfeld = ("{0} {1} {2} \n{3} {4} {5}\n{6} {7} {8}".format(
            self.feld[0][0],self.feld[0][1],self.feld[0][2],
            self.feld[1][0],self.feld[1][1],self.feld[1][2],
            self.feld[2][0],self.feld[2][1],self.feld[2][2])
        )
        return spielfeld

    def SpielfeldChange(self, eingabe):
        if(eingabe%3 == 0):
            i = (int)(eingabe/3-1)
        else:
            i = (int)(eingabe/3)
        if(self.feld[i][(int)(eingabe%3)-1] != 'X' and self.feld[i][(int)(eingabe%3)-1] != 'O'):
            self.feld[i][(int)(eingabe%3)-1] = self.Spieler()
            return

    def GleicheZeichen(self, eins, zwei, drei):
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
            if(self.GleicheZeichen(self.feld[0][i],self.feld[1][i],self.feld[2][i])):
                Gewonnen = True
                break
            elif(self.GleicheZeichen(self.feld[i][0],self.feld[i][1],self.feld[i][2])):
                Gewonnen = True
                break
        if(self.GleicheZeichen(self.feld[0][0],self.feld[1][1],self.feld[2][2])):
            Gewonnen = True      
        elif(self.GleicheZeichen(self.feld[0][2],self.feld[1][1],self.feld[2][0])):
            Gewonnen = True
        return Gewonnen

    def Spieler(self):
        XO = 'X'
        if(self.anzahlZuege%2==0):
            XO = 'X'    
        else:
            XO = 'O'
        return XO