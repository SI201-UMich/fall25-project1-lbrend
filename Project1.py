# name: Brendon Lee
# student ID: 47446397
# email: leebrendg@umich.edu
# collaborators: Gen AI
# solo project


import csv
import unittest


def read_penguin_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

        print("column1: ", data[0].keys(), )
        print("column2: ", data[1].keys(), "\n")
        print("sample row1: ",data[0], "\n")
        
        print("sample row2: ",data[1], "\n")
        print("total rows: ", len(data))
    return data



class PenguinTest(unittest.TestCase):
    def test_heaviest_species_by_island(self):
        #test cases with sample data for heaviest species by island

        test_sample_data = [
            {'island': 'Biscoe', 'species': 'Gentoo', 'body_mass_g': 'NA', 'sex': 'MALE'},
            {'island': 'Biscoe', 'species': 'Gentoo', 'body_mass_g': '5100', 'sex': 'FEMALE'},
            {'island': 'Biscoe', 'species': 'Adelie', 'body_mass_g': '3600', 'sex': 'FEMALE'},]
        

        expected = [
            {'island': 'Biscoe', 'heaviest_species': 'Gentoo', 'average_mass_g': 5100.0},]
        


        result = heaviest_species_by_island(test_sample_data)
        self.assertEqual(result, expected)

        



    def test_avg_mass_by_species(self):
        #test cases with sample data for average mass by species

        test_data = [
            {'species': 'Gentoo', 'body_mass_g': '5200', 'sex': 'MALE'},
            {'species': 'Gentoo', 'body_mass_g': 'NA', 'sex': 'MALE'},
            {'species': 'Adelie', 'body_mass_g': '3600', 'sex': 'FEMALE'},
            {'species': 'Adelie', 'body_mass_g': '4000', 'sex': 'NA'},   ]
        
        
        expected = [
            {'species': 'Gentoo', 'average_adult_mass_g': 5200.0},
            {'species': 'Adelie', 'average_adult_mass_g': 3600.0} ]
        

        
        result = avg_mass_by_species(test_data)
        self.assertEqual(result, expected)


def heaviest_species_by_island(penguins):
    
    

    mass_dict = {}
    

    for row in penguins:
        island = row['island']
        species = row['species']
        mass = row['body_mass_g']


        if mass and mass != 'NA':

            try:
                mass = float(mass)
                if island not in mass_dict:
                    mass_dict[island] = {}

                if species not in mass_dict[island]:
                    mass_dict[island][species] = []
                mass_dict[island][species].append(mass)


            except ValueError:
                pass


    results = []

    for island, sp_dict in mass_dict.items():
        max_avg, max_species = -1, None

        for species, masses in sp_dict.items():
            if masses:
                avg_mass = sum(masses) / len(masses)
                if avg_mass > max_avg:
                    max_avg = avg_mass
                    max_species = species


        results.append({'island': island, 'heaviest_species': max_species, 'average_mass_g': round(max_avg,2)})


    return results



def avg_mass_by_species(penguins):
    

    species_masses = {}


    for row in penguins:
        species = row['species']
        mass = row['body_mass_g']
        sex = row['sex']

        if species and mass and mass != 'NA' and sex and sex != 'NA':

            try:
                mass = float(mass)

                if species not in species_masses:
                    species_masses[species] = []
                species_masses[species].append(mass)

            except ValueError:
                pass


    results = []

    for species, masses in species_masses.items():
        avg = sum(masses) / len(masses)
        results.append({'species': species, 'average_mass_g': round(avg,2)})

    return results




def write_to_csv(filename, fieldnames, rows):

    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)




def main():


    data = read_penguin_data('penguins.csv')

    heaviest = heaviest_species_by_island(data)
    write_to_csv('heaviest_species_by_island.csv', ['island', 'heaviest_species', 'average_mass_g'], heaviest)

    avg_adult = avg_mass_by_species(data)
    write_to_csv('average_body_mass_by_species.csv', ['species', 'average_mass_g'], avg_adult)



if __name__ == "__main__":
   

    #unittest.main()

    main()


