import sublime
import sublime_plugin

class GoToLineCommand(sublime_plugin.TextCommand):
    def run(self, edit, line):
        self.view.run_command("goto_line", {"line": line})
        line_region = self.view.line(self.view.text_point(line - 1, 0))
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(line_region.begin()))
        self.view.show(line_region)
