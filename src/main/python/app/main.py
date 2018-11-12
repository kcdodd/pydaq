from fbs_runtime.application_context import ApplicationContext, cached_property
import sys

from app import dependencies, arg_parser, widgets
from server import api

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class AppContext(ApplicationContext):
  #-----------------------------------------------------------------------------
  def run(self):

    args = arg_parser.parse_args()

    if args.server is not None:

      print("Running as api server instance.")
      return api.run()

    else:

      stylesheet = self.get_resource('styles.qss')
      self.app.setStyleSheet(open(stylesheet).read())
      self.window.show()
      return self.app.exec_()

  #-----------------------------------------------------------------------------
  @cached_property
  def window(self):
    return widgets.MainWindow()

################################################################################
if __name__ == '__main__':

  appctx = AppContext()
  exit_code = appctx.run()

  sys.exit(exit_code)
