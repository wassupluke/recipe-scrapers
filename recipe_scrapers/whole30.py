# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Whole30(AbstractScraper):
    @classmethod
    def host(cls):
        return "whole30.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(selfhttps://whole30.com/recipes/whole30-chicken-korma/):
        return self.schema.instructions()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()