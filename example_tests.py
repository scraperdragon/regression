#!/usr/bin/env python

import unittest
from nose.tools import assert_equal
from os.path import join, dirname, abspath
import datetime

class ConvertTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run once before all tests in this test class."""
        cls.rows = [{'Commodity': 'Cheese',
                     'Origin': 'Moon',
                     'Figure': 2.0},
                    {'Commodity': 'Rust',
                     'Origin': 'Mars',
                     'Figure': 12.0}]


    def test_correct_number_of_rows(self):
        assert_equal(2, len(self.rows))

    def not_a_you_know_what(self):
        pass

    def test_first_row(self):
        assert_equal('Grapefruit (inc. pomelos)', self.rows[0]['Commodity'])
        assert_equal('Morocco', self.rows[0]['Origin'])
        assert_equal(1000.0, self.rows[0]['Figure'])

    def test_last_row(self):
        assert_equal('Potatoes', self.rows[-1]['Commodity'])
        assert_equal('Vietnam', self.rows[-1]['Origin'])
        assert_equal(440000.0, self.rows[-1]['Figure'])

    def test_sector(self):
        self.assertEqual(
            set([
                'Fresh Fruit',
                'Exotics',
                'Grains',
                'Nuts',
                'Vegetables',
                ]),
            set(row['Sector'] for row in self.rows))

    def test_commodities(self):
        self.assertEqual(
            set([
                'Brazil nuts, with shell',
                'Cashew nuts, with shell',
                'Almonds, with shell',
                'Apples',
                'Apricots',
                'Arecanuts',
                'Artichokes',
                'Asparagus',
                'Avocados',
                'Bananas',
                'Beans, green',
                'Berries Nes',
                'Blueberries',
                'Brazil nuts, with shell',
                'Cashewapple',
                'Cashew nuts, with shell',
                'Cauliflowers and broccoli',
                'Cherries',
                'Citrus fruit, nes',
                #'Cranberries', not for currently selected countries
                #'Currants',    not for currently selected countries
                'Dates',
                'Figs',
                'Fruit Fresh Nes',
                'Grapefruit (inc. pomelos)',
                'Grapes',
                'Groundnuts, with shell',
                'Hazelnuts, with shell',
                #'Kiwi fruit',  not for currently selected countries
                'Lemons and limes',
                'Maize',
                'Mangoes, mangosteens, guavas',
                'Mushrooms and truffles',
                'Nuts, nes',
                'Oranges',
                'Papayas',
                'Peaches and nectarines',
                'Pears',
                'Peas, green',
                'Pineapples',
                'Pistachios',
                'Plums and sloes',
                'Potatoes',
                'Raspberries',
                'Sour cherries',
                'Stone fruit, nes',
                'Strawberries',
                'Tangerines, mandarins, clementines, satsumas',
                'Tomatoes',
                'Walnuts, with shell',
                ]),
            set(row['Commodity'] for row in self.rows))

    def test_origin(self):
        self.assertEqual(
            set([
                "Angola",
                "Belize",
                "Benin",
                "Bolivia",
                "Brazil",
                "Burkina Faso",
                "China",
                "Dominican Republic",
                "El Salvador",
                "Ghana",
                "Guadeloupe",
                "Guinea",
                "Guinea-Bissau",
                "Honduras",
                "India",
                "Indonesia",
                "Ivory Coast",
                "Kenya",
                "Madagascar",
                "Malaysia",
                "Mali",
                "Mexico",
                "Morocco",
                "Mozambique",
                "Nigeria",
                "Peru",
                "Philippines",
                "Senegal",
                "Sri Lanka",
                "Tanzania",
                "Thailand",
                "Togo",
                "Vietnam",
                ]),
            set(row['Origin'] for row in self.rows))

    def test_source(self):
        self.assertEqual(
            set(['UN FAO']),
            set(row['Source'] for row in self.rows))

    def test_indicator(self):
        self.assertEqual(
            set([
                "Area Harvested",
                "Production",
                "Yield",
                ]),
            set(row['Indicator'] for row in self.rows))

    def test_caption_detail_always_total(self):
        self.assertEqual(
            set(['Total']),
            set(row['Caption Detail'] for row in self.rows))

    def test_frequency_always_annual(self):
        self.assertEqual(
            set(['Annual']),
            set(row['Frequency'] for row in self.rows))

    def test_measure(self):
        self.assertEqual(
            set([
                "tonnes",
                "100kg/hectare",
                "Hectares",
                ]),
            set(row['Measure'] for row in self.rows))

    def test_dates(self):
        self.assertEqual(
            set([datetime.date(year, 1, 1) for year in range(1961, 2012 + 1)]),
            set([row['Date'] for row in self.rows]))

    def test_all_figures_are_floats(self):
        all_figures = [row['Figure'] for row in self.rows]
        for figure in all_figures:
            self.assertIsInstance(figure, float)
