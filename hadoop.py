import subprocess
import os
import sys
from subprocess import PIPE


#installation of java
process_java= subprocess.Popen(["sudo","apt-get","install","default-jdk","-y"],stdin=PIPE,stdout=PIPE)

if process_java.returncode:
	out_java=process_java.communicate()[0]
	print(out_java.decode('ascii'))

else:
	out_java=process_java.communicate()[0]
	print(out_java.decode())
	
	print("JAVA VERSION..")
	process_java_2= subprocess.Popen(["java","-version"],stdin=PIPE,stdout=PIPE)
	version= process_java_2.communicate()[1]

	print("JAVA is installed")

#installation of ssh
process_ssh= subprocess.Popen(["sudo","apt-get","install","ssh","-y"],stdin=PIPE,stdout=PIPE)

if process_ssh.returncode:
	out_ssh=process_ssh.communicate()[0]
	print(out_ssh.decode('ascii'))
else:
	out_ssh=process_ssh.communicate()[0]
	print(out_ssh.decode())

	print("ssh is installed")

#installation of pdsh
process_pdsh= subprocess.Popen(["sudo","apt-get","install","pdsh","-y"],stdin=PIPE,stdout=PIPE)

if process_pdsh.returncode:
	out_pdsh=process_pdsh.communicate()[0]
	print(out_pdsh.decode('ascii'))
else:
	out_pdsh=process_pdsh.communicate()[0]
	print(out_pdsh.decode())

	print("pdsh is installed")

#downloading Hadoop distribution
process_hadoop_dist= subprocess.Popen(["wget","https://downloads.apache.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz"],stdin=PIPE,stdout=PIPE)

if process_hadoop_dist.returncode:
	out_hadoop_dist=process_hadoop_dist.communicate()[0]
	print(out_hadoop_dist.decode('ascii'))
else:
	out_hadoop_dist=process_hadoop_dist.communicate()[0]
	print(out_hadoop_dist.decode())

	print("hadoop_dist is installed")

#unpack hadoop_dist file and edit java_home
process_unpack= subprocess.Popen(["tar","-xvf","hadoop-3.3.0.tar.gz"],stdin=PIPE,stdout=PIPE)

if process_unpack.returncode:
	out_unpack=process_unpack.communicate()[0]
	print(out_unpack.decode('ascii'))
else:
	out_unpack=process_unpack.communicate()[0]
	print(out_unpack.decode())

	print("hadoop unpacked")


#configuration
def writeXML(filename,content):
	with open(filename,"w") as file:
		file.write('''
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
'''+content)

content=''' <configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>'''

writeXML("hadoop-3.3.0/etc/hadoop/core-site.xml",content)

content='''<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>'''

writeXML("hadoop-3.3.0/etc/hadoop/hdfs-site.xml",content)

print("configuration done")

count=0
process_pass1= subprocess.Popen(["ssh-keygen", "-t", "rsa", "-P", "''", "-f", "~/.ssh/id_rsa","-y"],stdin=PIPE,stdout=PIPE)

if process_pass1.returncode:
	out_pass1=process_pass1.communicate()[0]
	print(out_pass1.decode('ascii'))
else:
	out_pass1=process_pass1.communicate()[0]
	print(out_pass1.decode())
	count+=1

process_pass2= subprocess.Popen(["cat", "~/.ssh/id_rsa.pub", ">>", "~/.ssh/authorized_keys"],stdin=PIPE,stdout=PIPE)

if process_pass2.returncode:
	out_pass2=process_pass2.communicate()[0]
	print(out_pass2.decode('ascii'))
else:
	out_pass2=process_pass2.communicate()[0]
	print(out_pass2.decode())
	count+=1

process_pass3= subprocess.Popen(["chmod", "0600", "~/.ssh/authorized_keys"],stdin=PIPE,stdout=PIPE)

if process_pass3.returncode:
	out_pass3=process_pass3.communicate()[0]
	print(out_pass3.decode('ascii'))
else:
	out_pass3=process_pass3.communicate()[0]
	print(out_pass3.decode())
	count+=1

if count==3:
	print("passphraseless has been setup")


