# MongoChat

# Before shutdown
## rs.status
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T19:41:00.249Z"),
	"myState" : 1,
	"term" : NumberLong(4),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572637259, 1),
			"t" : NumberLong(4)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T19:40:59.876Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572637259, 1),
			"t" : NumberLong(4)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T19:40:59.876Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572637259, 1),
			"t" : NumberLong(4)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572637259, 1),
			"t" : NumberLong(4)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T19:40:59.876Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T19:40:59.876Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572637229, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572637229, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-10-29T20:38:20.543Z"),
		"termAtElection" : NumberLong(4),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572381474, 1),
			"t" : NumberLong(3)
		},
		"numVotesNeeded" : 1,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"newTermStartDate" : ISODate("2019-10-29T20:38:21.545Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T20:38:21.624Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "master:27017",
			"ip" : "172.31.32.125",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 255761,
			"optime" : {
				"ts" : Timestamp(1572637259, 1),
				"t" : NumberLong(4)
			},
			"optimeDate" : ISODate("2019-11-01T19:40:59Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572381500, 1),
			"electionDate" : ISODate("2019-10-29T20:38:20Z"),
			"configVersion" : 4,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "slave-1:27017",
			"ip" : "172.31.42.176",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 254983,
			"optime" : {
				"ts" : Timestamp(1572637249, 1),
				"t" : NumberLong(4)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572637249, 1),
				"t" : NumberLong(4)
			},
			"optimeDate" : ISODate("2019-11-01T19:40:49Z"),
			"optimeDurableDate" : ISODate("2019-11-01T19:40:49Z"),
			"lastHeartbeat" : ISODate("2019-11-01T19:40:58.989Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T19:40:58.989Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "master:27017",
			"syncSourceHost" : "master:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 4
		},
		{
			"_id" : 2,
			"name" : "slave-2:27017",
			"ip" : "172.31.31.149",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 254979,
			"optime" : {
				"ts" : Timestamp(1572637249, 1),
				"t" : NumberLong(4)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572637249, 1),
				"t" : NumberLong(4)
			},
			"optimeDate" : ISODate("2019-11-01T19:40:49Z"),
			"optimeDurableDate" : ISODate("2019-11-01T19:40:49Z"),
			"lastHeartbeat" : ISODate("2019-11-01T19:40:59.654Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T19:40:59.653Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "slave-1:27017",
			"syncSourceHost" : "slave-1:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 4
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572637259, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572637259, 1)
}
```

## rs.config
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 4,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "master:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "slave-1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "slave-2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db8a02bc07655afcc410d48")
	}
}
```

## screenshot
[Google Disk] https://drive.google.com/file/d/1xL3k0Bpi5JFmaQEkC2SQXGUkxXPRwJhB/view?usp=sharing

# After master shutdown
## rs.status
```
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T20:03:43.186Z"),
	"myState" : 2,
	"term" : NumberLong(5),
	"syncingTo" : "slave-1:27017",
	"syncSourceHost" : "slave-1:27017",
	"syncSourceId" : 1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572638615, 1),
			"t" : NumberLong(5)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T20:03:35.917Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572638615, 1),
			"t" : NumberLong(5)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T20:03:35.917Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572638615, 1),
			"t" : NumberLong(5)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572638615, 1),
			"t" : NumberLong(5)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T20:03:35.917Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T20:03:35.917Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572638605, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572638605, 1),
	"members" : [
		{
			"_id" : 0,
			"name" : "master:27017",
			"ip" : "172.31.32.125",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:03:41.898Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T19:49:25.886Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to master:27017 (172.31.32.125:27017) :: caused by :: Connection refused",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "slave-1:27017",
			"ip" : "172.31.42.176",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 256342,
			"optime" : {
				"ts" : Timestamp(1572638615, 1),
				"t" : NumberLong(5)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572638615, 1),
				"t" : NumberLong(5)
			},
			"optimeDate" : ISODate("2019-11-01T20:03:35Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:03:35Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:03:41.403Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:03:41.767Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572637765, 1),
			"electionDate" : ISODate("2019-11-01T19:49:25Z"),
			"configVersion" : 4
		},
		{
			"_id" : 2,
			"name" : "slave-2:27017",
			"ip" : "172.31.31.149",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 257018,
			"optime" : {
				"ts" : Timestamp(1572638615, 1),
				"t" : NumberLong(5)
			},
			"optimeDate" : ISODate("2019-11-01T20:03:35Z"),
			"syncingTo" : "slave-1:27017",
			"syncSourceHost" : "slave-1:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 4,
			"self" : true,
			"lastHeartbeatMessage" : ""
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572638615, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572638615, 1)
}
```

## rs.config
```{
	"_id" : "rs0",
	"version" : 4,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "master:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "slave-1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "slave-2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db8a02bc07655afcc410d48")
	}
}
```

## screenshot
[Google Disk] https://drive.google.com/file/d/1Rto7rPuvwF6GDubd0TPf-mWStCX-Flwb/view?usp=sharing
