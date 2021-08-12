from libqtile import widget
from settings.theme import colors, img


base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = {
    **base(),
    'linewidth': 0,
    'padding': 5,
}

text_box = lambda fontsize=20: {
    'font': 'Ubuntu Mono',
    'fontsize': fontsize,
    'padding': 5
}

def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )

workspaces = lambda: [
    widget.Sep(**separator),
    widget.GroupBox(
        **base(fg='dark'),
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['lime'],
        inactive=colors['dark'],
        rounded=False,
        highlight_method='block',
        this_current_screen_border=colors['dark'], #the actual monitor color
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    widget.Sep(**separator),
    widget.WindowName(
        **base(fg='lime'), #text for monitor position
        fontsize=12,
        padding=5
    ),
    widget.Sep(**separator),
]

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

laptop_widgets = [
    *workspaces(),
    widget.Systray(
        background=colors['dark'],
        padding=5
    ),
    widget.Sep(**separator),
    
    
    widget.CurrentLayoutIcon(
        foreground=colors['lime'],
        scale=0.65
        
    ),

    widget.CurrentLayout(
        foreground=colors['lime'],
        padding=5
    ),
    
    widget.Clock(
        foreground=colors['lime'],
        format='%d/%m/%Y - %H:%M '
    ),
]

monitor_widgets = [
    *workspaces(),
    widget.Sep(**separator),
    widget.Image(
        filename=img['bar4']
    ),
    widget.CurrentLayoutIcon(
        **base(bg='lime'),
        scale=0.65
    ),
    widget.CurrentLayout(
        **base(bg='lime'),
        padding=5
        
    ),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
