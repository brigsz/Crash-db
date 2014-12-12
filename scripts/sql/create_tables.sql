USE [Crash]
GO

/****** Object:  Table [dbo].[Rollup]    Script Date: 12/11/2014 17:20:58 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Rollup](
	[id] [int] NOT NULL,
	[date] [date] NULL,
	[pedestrian] [bit] NULL,
	[bicycle] [bit] NULL,
	[motorcycle] [bit] NULL,
	[improper_restraint] [bit] NULL,
	[dui] [bit] NULL,
	[intersection] [bit] NULL,
	[animal_wild] [bit] NULL,
	[animal_domestic] [bit] NULL,
	[rollover] [bit] NULL,
	[commercial_vehical] [bit] NULL,
	[teenager] [bit] NULL,
	[elder] [bit] NULL,
	[dark] [bit] NULL
) ON [PRIMARY]

CREATE TABLE [dbo].[Driver](
	[id] [int] NOT NULL,
	[date] [date] NULL,
	[vehicle_count] [int] NULL,
	[contributing_cause] [nchar](100) NULL,
	[alternate_cause] [nchar](100) NULL,
	[driver_condition] [nchar](100) NULL,
	[driver_distraction] [nchar](100) NULL
) ON [PRIMARY]

CREATE TABLE [dbo].[Crash](
	[id] [int] NOT NULL,
	[date] [date] NULL,
	[year] [int] NULL,
	[month] [int] NULL,
	[day] [int] NULL,
	[hour] [int] NULL,
	[minute] [int] NULL,
	[construction] [bit] NULL,
	[weather_condition] [nchar](50) NULL,
	[road_condition] [nchar](50) NULL,
	[event] [nchar](100) NULL,
	[collision_type] [nchar](50) NULL,
	[severity] [nchar](50) NULL,
	[case_number] [nchar](25) NULL,
	[officer_name] [nchar](100) NULL,
	[officer_department] [nchar](100) NULL,
	[road_name] [nchar](100) NULL,
	[route_number] [int] NULL,
	[milepost] [numeric](4, 4) NULL,
	[city] [nchar](50) NULL,
	[county] [nchar](25) NULL,
	[utm_x] [float] NULL,
	[utm_y] [float] NULL
) ON [PRIMARY]

GO


