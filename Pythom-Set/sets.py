'''
Scenario: You are working as a backend developer for a startup. Your web server
generates logs containing the IP addresses of users who visit your website. You
have been given two lists of IP addresses: one for visitors on Saturday and one for
visitors on Sunday. The marketing team wants to analyze user retention and reach
over the weekend.

Write a Python script using sets to calculate and print the following:
The total number of unique visitors over the entire weekend.
The IP addresses of users who visited on both Saturday and Sunday (Loyal visitors).
The IP addresses of users who visited on Saturday but not on Sunday (Dropped-off
visitors).

saturday_ips = ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.2',
'10.0.0.5']
sunday_ips = ['10.0.0.5', '172.16.0.2', '192.168.1.100', '10.0.0.10']


'''

saturday_ips = {'192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.2', '10.0.0.5'}
sunday_ips = {'10.0.0.5', '172.16.0.2', '192.168.1.100', '10.0.0.10'}


unique_ip = saturday_ips | sunday_ips
loyal_visitor = saturday_ips & sunday_ips

dropped_off =  saturday_ips - sunday_ips

print(unique_ip)
print(loyal_visitor)
print(dropped_off)
