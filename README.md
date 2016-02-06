# Paro
Quickly create boot scripts for your servers, packing in as much data as possible. Paro will automatically optimize your data, allowing you to transfer more and download less.

## Amazon EC2
Amazon's "user data scripts" have a 16KB limit. Use this to transfer configurations, software, and data files. Automatic compression lets you make the most of this space, while avoiding bandwidth charges for external downloads.

[Amazon EC2 User Data Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)