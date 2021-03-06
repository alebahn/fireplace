from ..utils import *


##
# Minions

# Fel Reaver
class GVG_016:
	events = Play(OPPONENT).on(Mill(CONTROLLER, 3))


# Hobgoblin
class GVG_104:
	events = OWN_MINION_PLAY.on(
		lambda self, player, card, *args: card.atk == 1 and Buff(card, "GVG_104a")
	)


# Piloted Sky Golem
class GVG_105:
	deathrattle = Summon(CONTROLLER, RandomMinion(cost=4))


# Junkbot
class GVG_106:
	events = Death(FRIENDLY + MECH).on(Buff(SELF, "GVG_106e"))


# Enhance-o Mechano
class GVG_107:
	def play(self):
		for target in self.controller.field.exclude(self):
			tag = random.choice((GameTag.WINDFURY, GameTag.TAUNT, GameTag.DIVINE_SHIELD))
			yield SetTag(target, {tag: True})


# Recombobulator
class GVG_108:
	def play(self, target):
		return Morph(TARGET, RandomMinion(cost=target.cost))


# Clockwork Giant
class GVG_121:
	cost = lambda self, i: i - len(self.controller.opponent.hand)
