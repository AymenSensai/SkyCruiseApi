import os

os.environ['PYTEST_RUNNING'] = 'true'

from skycruise.airline.tests.fixtures import *  # noqa: F401, F403, E402
from skycruise.flight.tests.fixtures import *  # noqa: F401, F403, E402
from skycruise.general.tests.fixtures import *  # noqa: F401, F403, E402
from skycruise.location.tests.fixtures import *  # noqa: F401, F403, E402
from skycruise.reservation.tests.fixtures import *  # noqa: F401, F403, E402
from skycruise.users.tests.fixtures import *  # noqa: F401, F403, E402
