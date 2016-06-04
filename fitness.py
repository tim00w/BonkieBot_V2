class Oefening:

    def __init__(self, naam):
        """
        DocString
        """
        self.naam = naam
        self.series = []
        self.opmerking = []
        
    def __str__(self):
        return "{}\n{}\n\n{}"
    
    def nieuwe_set(self, reps, gewicht):
        """
        DocString
        """
        self.series.append(Set(reps, gewicht))
        

    def opmerking(self, tekst):
        """
        DocString
        """
        self.opmerking.append(tekst)
        

class SuperSet:
    
    def __init__():
        """
        DocString
        """
        return

class Set:
    
    def __init__(self, herhalingen, gewicht, eenheid='kg'):
        """
        DocString
        """
        self.herhalingen = herhalingen
        self.gewicht = gewicht
        self.eenheid = eenheid
        
        
    def __str__(self):
        return 'herhalingen: {}\ngewicht: {} {}'.format(self.herhalingen, self.gewicht, self.eenheid)
    
    def __repr__(self):
        return "({}, {})".format(self.herhalingen, self.gewicht)

class Training:
    
    def __init__():
        """
        DocString
        """
        return
