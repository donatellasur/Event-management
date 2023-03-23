from service.Serv import Serv
from repository.Repo import Repo
from domain.validators import Validator
from tests import runTests

from console.console import Console

val = Validator()
repo = Repo()
srv = Serv(repo, val)

ui = Console(srv)
runTests()
ui.showUI()
