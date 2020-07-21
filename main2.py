from scenes.game import Game
import configuration as config
import const.colors as colors
import helpers.files as hfiles
import const.files as cfiles

pkmnMatrix = hfiles.readPkmnInMatrix(cfiles.PKMN_JSON_PATH, config.MAX_COLUMNS)

mygame = Game(config, colors, pkmnMatrix)
mygame.initGame()