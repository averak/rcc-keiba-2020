# -*- coding: utf-8 -*-


class Factory:
    def self.build(**config):
        for attr_config in config:
            print(attr_config)
