import sublime
import sublime_plugin

class AddRegionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Iterate through each selected region (if multiple selections exist)
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                selected_text = self.view.substr(region)
                # Get the starting and ending positions of the selected region
                start_pos = region.begin()
                end_pos = region.end()

                # Insert the #pragma region and #pragma endregion
                self.view.insert(edit, start_pos, "#pragma region\n")
                self.view.insert(edit, end_pos + len("#pragma region\n"), "\n#pragma endregion\n")

                # Update the region to include the added pragma lines
                new_end_pos = end_pos + len("#pragma region\n") + len("#pragma endregion\n")
                self.view.sel().add(sublime.Region(start_pos, new_end_pos))
