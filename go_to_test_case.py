import sublime
import sublime_plugin
import re

class GoToFunctionBodyCommand(sublime_plugin.TextCommand):
    def run(self, edit, function_name):
        # Search for the function definition
        pattern = r'\b{}\b\s*\([^)]*\)\s*\{{'.format(re.escape(function_name))
        regions = self.view.find_all(pattern)
        if regions:
            function_start = regions[0].end()
            # Find the end of the opening brace
            brace_region = self.view.find(r'\{', function_start)
            if brace_region:
                # Move the cursor to the next line after the opening brace
                next_line_start = self.view.line(brace_region.end()).end() + 1
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(next_line_start, next_line_start))
                self.view.show_at_center(next_line_start)
        else:
            sublime.status_message("Function '{}' not found".format(function_name))
