import pikeblock

class RegressionCheck(pikeblock.Case):
    def set_up(self):
        self.run_these = [self.correct_number_of_rows,
                          self.first_row,
                          self.sector]
        self.rows = [{'Commodity': 'Cheese',
                      'Origin': 'Moon',
                      'Figure': 2.0,
                      'Sector': '005'},
                     {'Commodity': 'Rust',
                      'Origin': 'Mars',
                      'Figure': 12.0,
                      'Sector': '001'}]

    def correct_number_of_rows(self):
        return len(self.rows)

    def first_row(self):
        return (self.rows[0]['Commodity'],
                self.rows[0]['Origin'],
                self.rows[0]['Figure'])

    def sector(self):
        return set(row['Sector'] for row in self.rows)

if __name__ == "__main__":
    RegressionCheck().save()

TestSequence = RegressionCheck().all_tests()
