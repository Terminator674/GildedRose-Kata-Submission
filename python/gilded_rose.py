# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
CONJURED_PREFIX = "Conjured"

MAX_QUALITY = 50
MIN_QUALITY = 0


class ItemUpdater(object):
    def update(self, item):
        self.update_quality(item)
        self.update_sell_in(item)
        if item.sell_in < 0:
            self.update_quality_after_sell_by(item)

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_quality(self, item):
        self.decrease_quality(item, 1)

    def update_quality_after_sell_by(self, item):
        self.decrease_quality(item, 1)

    def increase_quality(self, item, amount):
        item.quality = min(MAX_QUALITY, item.quality + amount)

    def decrease_quality(self, item, amount):
        item.quality = max(MIN_QUALITY, item.quality - amount)


class AgedBrieUpdater(ItemUpdater):
    def update_quality(self, item):
        self.increase_quality(item, 1)

    def update_quality_after_sell_by(self, item):
        self.increase_quality(item, 1)


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class BackstagePassUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.sell_in <= 5:
            self.increase_quality(item, 3)
        elif item.sell_in <= 10:
            self.increase_quality(item, 2)
        else:
            self.increase_quality(item, 1)

    def update_quality_after_sell_by(self, item):
        item.quality = 0


class ConjuredUpdater(ItemUpdater):
    def update_quality(self, item):
        self.decrease_quality(item, 2)

    def update_quality_after_sell_by(self, item):
        self.decrease_quality(item, 2)


UPDATERS_BY_NAME = {
    AGED_BRIE: AgedBrieUpdater(),
    SULFURAS: SulfurasUpdater(),
    BACKSTAGE_PASSES: BackstagePassUpdater(),
}
DEFAULT_UPDATER = ItemUpdater()


def get_updater(item_name):
    if item_name in UPDATERS_BY_NAME:
        return UPDATERS_BY_NAME[item_name]
    if item_name.startswith(CONJURED_PREFIX):
        return ConjuredUpdater()
    return DEFAULT_UPDATER


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            get_updater(item.name).update(item)