# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def update(self, item):
        GildedRose([item]).update_quality()
        return item

    # normal items
    def test_normal_item_quality_decreases_by_one(self):
        item = self.update(Item("Normal Item", 10, 20))
        self.assertEqual(item.quality, 19)
        self.assertEqual(item.sell_in, 9)

    def test_normal_item_degrades_twice_as_fast_after_sell_by(self):
        item = self.update(Item("Normal Item", 0, 20))
        self.assertEqual(item.quality, 18)

    def test_normal_item_quality_never_negative(self):
        item = self.update(Item("Normal Item", 5, 0))
        self.assertEqual(item.quality, 0)

    # aged brie
    def test_aged_brie_increases_in_quality(self):
        item = self.update(Item("Aged Brie", 10, 20))
        self.assertEqual(item.quality, 21)

    def test_aged_brie_increases_twice_as_fast_after_sell_by(self):
        item = self.update(Item("Aged Brie", 0, 20))
        self.assertEqual(item.quality, 22)

    def test_aged_brie_quality_never_above_fifty(self):
        item = self.update(Item("Aged Brie", 10, 50))
        self.assertEqual(item.quality, 50)

    # sulfuras
    def test_sulfuras_quality_never_changes(self):
        item = self.update(Item("Sulfuras, Hand of Ragnaros", 5, 80))
        self.assertEqual(item.quality, 80)

    def test_sulfuras_sell_in_never_changes(self):
        item = self.update(Item("Sulfuras, Hand of Ragnaros", 5, 80))
        self.assertEqual(item.sell_in, 5)

    # backstage passes
    def test_backstage_passes_increase_by_one_when_far_out(self):
        item = self.update(Item("Backstage passes to a TAFKAL80ETC concert", 15, 20))
        self.assertEqual(item.quality, 21)

    def test_backstage_passes_increase_by_two_at_ten_days(self):
        item = self.update(Item("Backstage passes to a TAFKAL80ETC concert", 10, 20))
        self.assertEqual(item.quality, 22)

    def test_backstage_passes_increase_by_three_at_five_days(self):
        item = self.update(Item("Backstage passes to a TAFKAL80ETC concert", 5, 20))
        self.assertEqual(item.quality, 23)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        item = self.update(Item("Backstage passes to a TAFKAL80ETC concert", 0, 20))
        self.assertEqual(item.quality, 0)

    def test_backstage_passes_never_above_fifty(self):
        item = self.update(Item("Backstage passes to a TAFKAL80ETC concert", 5, 49))
        self.assertEqual(item.quality, 50)

    # adding conjured
    def test_conjured_item_degrades_twice_as_fast(self):
        item = self.update(Item("Conjured Mana Cake", 10, 20))
        self.assertEqual(item.quality, 18)

    def test_conjured_item_degrades_four_times_after_sell_by(self):
        item = self.update(Item("Conjured Mana Cake", 0, 20))
        self.assertEqual(item.quality, 16)

    def test_conjured_item_quality_never_negative(self):
        item = self.update(Item("Conjured Mana Cake", 5, 1))
        self.assertEqual(item.quality, 0)

    def test_any_conjured_item_name_recognised(self):
        item = self.update(Item("Conjured Sword", 10, 10))
        self.assertEqual(item.quality, 8)


if __name__ == '__main__':
    unittest.main()