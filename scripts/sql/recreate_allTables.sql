USE [Crash]
GO

/****** Object:  Table [dbo].[Crash]    Script Date: 12/11/2014 20:27:35 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Crash]') AND type in (N'U'))
DROP TABLE [dbo].[Crash]
GO

USE [Crash]
GO

/****** Object:  Table [dbo].[Crash]    Script Date: 12/11/2014 20:27:35 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Crash](
	[id] [int] IDENTITY NOT NULL,
	[crash_id] [int] NOT NULL,
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
	[case_number] [nchar](400) NULL,
	[officer_name] [nchar](100) NULL,
	[officer_department] [nchar](100) NULL,
	[road_name] [nchar](100) NULL,
	[route_number] [int] NULL,
	[milepost] [float] NULL,
	[city] [nchar](50) NULL,
	[county] [nchar](25) NULL,
	[utm_x] [float] NULL,
	[utm_y] [float] NULL,
 CONSTRAINT [PK_Crash] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

USE [Crash]
GO

/****** Object:  Table [dbo].[Driver]    Script Date: 12/11/2014 20:25:10 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Driver]') AND type in (N'U'))
DROP TABLE [dbo].[Driver]
GO

USE [Crash]
GO

/****** Object:  Table [dbo].[Driver]    Script Date: 12/11/2014 20:25:10 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Driver](
    [id] [int] IDENTITY NOT NULL,
    [driver_id] [int] NOT NULL,
    [date] [date] NULL,
    [vehicle_count] [int] NULL,
    [contributing_cause] [nchar](100) NULL,
    [alternate_cause] [nchar](100) NULL,
    [driver_condition] [nchar](100) NULL,
    [driver_distraction] [nchar](100) NULL
 CONSTRAINT [PK_Driver] PRIMARY KEY CLUSTERED
(
    [id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


USE [Crash]
GO

/****** Object:  Table [dbo].[Rollup]    Script Date: 12/11/2014 20:26:16 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Rollup]') AND type in (N'U'))
DROP TABLE [dbo].[Rollup]
GO

USE [Crash]
GO

/****** Object:  Table [dbo].[Rollup]    Script Date: 12/11/2014 20:26:16 ******/
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
	[dark] [bit] NULL,
 CONSTRAINT [PK_Rollup] PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


