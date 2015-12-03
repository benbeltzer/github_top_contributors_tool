# test_get_top_ten_contributors

from gh_request import *

astropy_contributors = ["eteq", "mdboom", "astrofrog", "embray", "taldcroft",
	"mhvk", "mdmueller", "adrn", "keflavich", "larrybradley"]

def test_get_top_ten_contributors():
    print "Testing get_top_ten_contributors"
    contributors_json = get_contributors("astropy", "astropy")
    contributors = get_contributor_details(contributors_json)
    for i in xrange(10):
    	(name, count) = contributors[i]
    	assert(name == astropy_contributors[i])
    print "Passed test"

test_get_top_ten_contributors()