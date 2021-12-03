import sys

class KronaTreePlugin:
    def input(self, filename):
       self.kronafile = open(filename, 'r')

    def run(self):
       self.kingdoms = set()
       self.phyla = set()
       self.classes = set()
       self.orders = set()
       self.families = set()
       self.genera = set()
       self.species = set()
       self.strains = set()

       for line in self.kronafile:
         contents = line.strip().split('\t')
         if (len(contents) > 3):
           self.kingdoms.add(contents[3])
         if (len(contents) > 4):
           self.phyla.add(contents[4])
         if (len(contents) > 5):
           self.classes.add(contents[5])
         if (len(contents) > 6):
           self.orders.add(contents[6])
         if (len(contents) > 7):
           self.families.add(contents[7])
         if (len(contents) > 8):
           self.genera.add(contents[8])
         if (len(contents) > 9):
           self.species.add(contents[9])
         if (len(contents) > 10):
           self.strains.add(contents[10])
         if (len(contents) > 11):
             print("WARNING: MORE THAN 11 ENTRIES: "+line.strip().replace('\t', '|'))


    def output(self, filename):
       outkingdom = open(filename+".kingdom.txt", 'w')
       for kingdom in self.kingdoms:
           outkingdom.write(kingdom+"\n")
       outphylum = open(filename+".phylum.txt", 'w')
       for phylum in self.phyla:
           outphylum.write(phylum+"\n")
       outclass = open(filename+".class.txt", 'w')
       for theclass in self.classes:
           outclass.write(theclass+"\n")
       outorder = open(filename+".order.txt", 'w')
       for order in self.orders:
           outorder.write(order+"\n")
       outfamily = open(filename+".family.txt", 'w')
       for family in self.families:
           outfamily.write(family+"\n")
       outgenus = open(filename+".genus.txt", 'w')
       for genus in self.genera:
           outgenus.write(genus+"\n")
       outspecies = open(filename+".species.txt", 'w')
       for speci in self.species:
           outspecies.write(speci+"\n")
       outstrain = open(filename+".strain.txt", 'w')
       for strain in self.strains:
           outstrain.write(strain+"\n")
