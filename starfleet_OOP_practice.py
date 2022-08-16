#Danial Syed
class CrewMember:
    def __init__(self, crew_id, last_name, first_name, rank):
        self.CrewMember = CrewMember
        self.crew_id = crew_id
        self.last_name = last_name
        self.first_name = first_name
        self.rank = rank
        if last_name == '':
            set_last_name = ''
        else:
            set_last_name = last_name
        if first_name == '':
            set_first_name = ''
        else:
            set_first_name = first_name
        if rank == '':
            set_rank = ''
        else:
            set_rank = rank
        self.stats = ([], [], [])
    def get_crew_id(self):
        return self.crew_id
    def get_last_name(self):
        return self.last_name
    def get_first_name(self):
        return self.first_name
    def get_rank(self):
        return self.rank
    def get_stats(self):
        return self.stats
    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
        return 
    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
    def set_rank(self, new_rank):
        self.rank = new_rank
    #Adds integers to stats tuple based on if it is P J or R
    #Integer is number added and string is the P J or R
    #A new version of self.stats is returned with the added number
    def add_stats(self, integer, string):
        if string == 'P':
            self.stats[0].append(integer)
        elif string == 'J':
            self.stats[1].append(integer)
        elif string == 'R':
            self.stats[2].append(integer)
        return self.stats
    #takes average of the number within stats based off P J or R
    #no parameters
    #a final tuple of average stats for each category is returned
    def average_stats(self):
        final = []
        PT = 0
        JT = 0
        RR = 0
        counter = 0
        for ele in self.stats[0]:
            if type(ele) == int:
                PT += ele
                counter += 1
        if PT != 0:
            PT_int = PT // counter
            PT_list = [round(PT_int)]
            final.append(PT_list)
            counter = 0
        else:
            final.append(0)
        for ele in self.stats[1]:
            if type(ele) == int:
                JT += ele
                counter += 1
        if JT != 0:
            JT_int = JT // counter
            JT_list = [round(JT_int)]
            final.append(JT_list)
            counter = 0
        else:
            final.append(0)
        for ele in self.stats[2]:
            if type(ele) == int:
                RR += ele
                counter += 1
        if RR != 0:
            RR_int = RR // counter
            RR_list = [round(RR_int)]
            final.append(RR_list)
        else:
            final.append(0)
            self.final = final
        return final
    def __str__(self):
        self.crew_id = str(self.crew_id)
        self.stats = str(self.stats)
        return "ID: " + self.crew_id+ '\n' + "Stats: " + self.stats+'\n'
class StarshipCrew(CrewMember):
    def __init__(self, starship_name, manufactured_year, ship_class, start_date_of_current_mission):
        self.crew = []
        self.starship_name = starship_name
        self.manufactured_year = manufactured_year
        self.ship_class = ship_class
        self.start_date_of_current_mission = start_date_of_current_mission
        #CrewMember.__init__(self, self.crew_id, self.last_name, self.first_name, self.rank)
    def get_crew(self):
        return self.crew
    def print_crew(self):
        for ele in self.crew:
            print(ele)
    def count(self):
        total_members = 0
        for ele in crew[::4]:
            total_members += 1
        return total_members
    def count_crew_rank(self, rank):
        total_same_rank = 0
        for ele in CrewMember:
            if ele == self.rank:
                total_same_rank += 1
        return total_same_rank
    def add_crew(self, CrewMember):
        self.crew.append(CrewMember)
    def __str__(self):
        self.manufactured_year = str(self.manufactured_year)
        self.start_date_of_current_mission = str(self.start_date_of_current_mission)
        return self.starship_name + ' '+ self.manufactured_year + ' ' + self.ship_class + ' ' + self.start_date_of_current_mission
if __name__ == '__main__':
    member = CrewMember(3, 'James', 'John', 'Commander',)
    member.add_stats(90,"J")
    member.add_stats(22,"J")
    member.add_stats(42,"P")
    print(member)
    starship = StarshipCrew('Trek', 1992, 'Cool', 12/12/2020)
    starship.add_crew(member)
    print(starship)
