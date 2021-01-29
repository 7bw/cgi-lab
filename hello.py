
#!/usr/bin/env python3

import os
import json

print(json.dumps(dict(os.environ), indent=2))
print(os.environ.get("QUERY_STRING"))
print(os.environ.get("HTTP_USER_AGENT"))
