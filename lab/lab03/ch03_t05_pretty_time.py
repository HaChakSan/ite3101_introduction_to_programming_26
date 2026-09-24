from datetime import datetime

now = datetime.now()

print('%02d/%02d/%04d' % (now.hour, now.minute, now.second))
from datetime import datetime

now = datetime.now()

# Print the time formatted as hh:mm:ss
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))