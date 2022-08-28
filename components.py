from discord.ui import View, button, Item
from discord import Button, ButtonStyle, Interaction


# This class doesn't work just yet, but I'm hoping I can get it to, soon
class OneButtonView(View):
    def __init__(self, button_label: str, message_label: str, next_view, *items: Item):
        super().__init__(*items)
        self.button_label: str = button_label
        self.message_label: str = message_label
        self.next_view: OneButtonView | None = next_view

    @button(label='', style=ButtonStyle.primary)
    async def button_callback(self, button: Button, interaction: Interaction):
        button.label = self.button_label
        button.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.response.send_message(self.message_label, view=self.next_view)


class StartView(View):
    @button(label="Okay, let's go!", style=ButtonStyle.primary)
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_message("Alright then, let's begin!", view=PastView())


class PastView(View):
    @button(label="Card 1: Past", style=ButtonStyle.primary)
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_message("I don't have any cards set up yet, so I can't see the past.",
                                                view=PresentView())


class PresentView(View):
    @button(label="Card 2: Present", style=ButtonStyle.primary)
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_message("I don't have any cards set up yet, so I can't see the present.",
                                                view=FutureView())


class FutureView(View):
    @button(label="Card 3: Future", style=ButtonStyle.primary)
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_message("I don't have any cards set up yet, so I can't see the future.",
                                                view=PastPresentFutureView())


class PastPresentFutureView(View):
    @button(label="Let's see all the cards", style=ButtonStyle.primary)
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_message("I'm sorry I couldn't have been more helpful, darling. Come back when "
                                                "Trisk codes some more!")
