import os
from process import Process
from colors import Colors

TIMEOUT_GIT = 90 # Timeout for GIT commands

class Opponent:
  """
  Represents the implementation of our classroom opponents.
  """

  def __init__(self, root_path, team_name, repo_url, clone_path, exe_path, timeout):
    self.root_path  = root_path
    self.name       = team_name
    self.repo_url   = repo_url
    self.clone_path = clone_path
    self.exe_path   = exe_path
    self.timeout    = timeout

  def build(self):
    """
    Executes opponent's Makefile to build an executable.
    """
    print Colors.OKBLUE + Colors.BOLD + 'BUILDING \t ' + self.name + Colors.ENDC
    os.chdir(self.clone_path)
    ps = Process(['make'], TIMEOUT_GIT)
    ps.Run()
    os.chdir(self.root_path)
    return ps.output()

  def clone(self):
    """
    Clones opponent's source code from Github.
    """
    print Colors.OKBLUE + Colors.BOLD + 'CLONING \t ' + self.name + Colors.ENDC
    ps = Process(['git', 'clone', self.repo_url, self.clone_path], TIMEOUT_GIT)
    ps.Run()
    return ps.output()

  def fetch(self):
    """
    Fetches updates from Github.
    """
    print Colors.OKBLUE + Colors.BOLD + 'FETCHING \t ' + self.name + Colors.ENDC
    os.chdir(self.clone_path)
    ps = Process(['git', 'fetch'], TIMEOUT_GIT)
    ps.Run()
    os.chdir(self.root_path)
    return ps.output()

  def pull(self):
    """
    Pulls updates from Github.
    """
    print Colors.OKBLUE + Colors.BOLD + 'PULLING \t ' + self.name + Colors.ENDC
    os.chdir(self.clone_path)
    ps = Process(['git', 'pull'], TIMEOUT_GIT)
    ps.Run()
    os.chdir(self.root_path)
    return ps.output()

  def run(self, input_path):
    """
    Executes opponent's SAT Solver with specified input path. If the executable
    does not exist, an error message is returned.

    input_path -- the text file to run thru SAT Solver
    """
    print Colors.OKBLUE + Colors.BOLD + 'RUNNING \t ' + self.name + Colors.ENDC
    executable = self.clone_path + self.exe_path
    if os.path.isfile(executable):
      ps = Process([self.clone_path + self.exe_path, input_path], self.timeout)
      ps.Run()
      return ps.output().split('\n')[0]
    else:
      return 'EXECUTABLE NOT FOUND\n'

  @staticmethod
  def setup_opponents(root_path, timeout):
    """
    Initializes Opponent objects for each opponent in our course.
    """
    opponents = [];
    opponents.append(Opponent(
        root_path,
        'CompUtahs', 
        'https://github.com/CompUtahs/sat-solver.git',
        'opponents/computahs',
        '/dpll_solver',
        timeout
      )
    )
    opponents.append(Opponent(
        root_path,
        'TeamNighthawk', 
        'https://github.com/TeamNighthawk/sat.git',
        'opponents/nighthawk',
        '/bin/satsolv',
        timeout
      )
    )
    opponents.append(Opponent(
        root_path,
        'SegmentationFaults', 
        'https://github.com/michaelandersonb/segmentationfaults.git',
        'opponents/segfaults',
        '/solver',
        timeout
      )
    )
    opponents.append(Opponent(
        root_path,
        'Toianoke', 
        'https://github.com/Toianoke/SAT.git',
        'opponents/taianoke',
        '/sat',
        timeout
      )
    )
    return opponents  
