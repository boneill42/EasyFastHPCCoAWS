import sys
import io

# Create the new config file for writing
config = io.open(sys.argv[1], 'w')

# Read the lines from the template, substitute the values, and write to the new config file
for line in io.open('/home/ec2-user/cassandra.yaml.template', 'r'):
    line = line.replace('$cluster_name', sys.argv[2])
    line = line.replace('$cassandra_seeds', sys.argv[3])
    line = line.replace('$private_ip', sys.argv[4])
    config.write(line)

# Close the files
config.close()
