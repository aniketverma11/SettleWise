import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from admin_interface.models import Theme

def configure_settlewise_theme(theme_name):
    """Configures or updates a theme with the exact provided SettleWise data."""
    theme, created = Theme.objects.get_or_create(name=theme_name)
    
    if not created:
        print(f"Updating existing theme: '{theme_name}'")
    else:
        print(f"Creating new theme: '{theme_name}'")

    # Provided Theme Data
    theme.active = True
    theme.title = 'SettleWise administration'
    theme.title_color = '#156641'
    theme.title_visible = True
    
    # Logo & Favicon
    # Note: These paths assume files exist in your media directory 
    # as per django-admin-interface upload structure.
    theme.logo = 'admin-interface/logo/logo-removebg-preview_1.png'
    theme.logo_color = '#FFFFFF'
    theme.logo_max_width = 400
    theme.logo_max_height = 50
    theme.logo_visible = True
    theme.favicon = 'admin-interface/favicon/logo-removebg-preview_1.png'
    
    # Environment
    theme.env_name = 'development'
    theme.env_color = '#E74C3C'
    theme.env_visible_in_header = True
    theme.env_visible_in_favicon = True
    
    # Language Chooser
    theme.language_chooser_active = True
    theme.language_chooser_control = 'default-select'
    theme.language_chooser_display = 'code'
    
    # CSS - Header
    theme.css_header_background_color = '#ffffff'
    theme.css_header_text_color = '#156641'
    theme.css_header_link_color = '#156641'
    theme.css_header_link_hover_color = '#dfebe5'
    
    # CSS - Modules
    theme.css_module_background_color = '#44B78B'
    theme.css_module_background_selected_color = '#FFFFCC'
    theme.css_module_text_color = '#FFFFFF'
    theme.css_module_link_color = '#FFFFFF'
    theme.css_module_link_selected_color = '#FFFFFF'
    theme.css_module_link_hover_color = '#C9F0DD'
    theme.css_module_rounded_corners = True
    
    # CSS - Generic Links
    theme.css_generic_link_color = '#0C3C26'
    theme.css_generic_link_hover_color = '#156641'
    theme.css_generic_link_active_color = '#29B864'
    
    # CSS - Buttons
    theme.css_save_button_background_color = '#0C4B33'
    theme.css_save_button_background_hover_color = '#0C3C26'
    theme.css_save_button_text_color = '#FFFFFF'
    
    theme.css_delete_button_background_color = '#BA2121'
    theme.css_delete_button_background_hover_color = '#A41515'
    theme.css_delete_button_text_color = '#FFFFFF'
    
    # Related Modal
    theme.related_modal_active = True
    theme.related_modal_background_color = '#000000'
    theme.related_modal_background_opacity = '0.3'
    theme.related_modal_rounded_corners = True
    theme.related_modal_close_button_visible = True
    
    # List Filter
    theme.list_filter_highlight = True
    theme.list_filter_dropdown = True
    theme.list_filter_sticky = True
    theme.list_filter_removal_links = True
    
    # Form/Apps Logic
    theme.foldable_apps = True
    theme.show_fieldsets_as_tabs = False
    theme.show_inlines_as_tabs = False
    theme.collapsible_stacked_inlines = False
    theme.collapsible_stacked_inlines_collapsed = True
    theme.collapsible_tabular_inlines = False
    theme.collapsible_tabular_inlines_collapsed = True
    theme.recent_actions_visible = True
    theme.form_actions_sticky = True
    theme.form_submit_sticky = True
    theme.form_pagination_sticky = True
    
    theme.save()
    
    # Deactivate other themes if this one is set to active
    Theme.objects.exclude(pk=theme.pk).update(active=False)
    
    print(f"✅ Theme '{theme_name}' has been successfully configured with your exact data!")

def main():
    print("--- Settlewise Theme configuration Tool ---")
    
    # List existing themes
    existing_themes = list(Theme.objects.values_list('name', flat=True))
    if existing_themes:
        print(f"Existing themes: {', '.join(existing_themes)}")
    else:
        print("No themes found.")

    default_name = "SettleWise"
    name = input(f"Enter theme name to create/update (default: '{default_name}'): ").strip()
    
    if not name:
        name = default_name
        
    configure_settlewise_theme(name)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
