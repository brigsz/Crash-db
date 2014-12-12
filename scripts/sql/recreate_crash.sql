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
	[case_number] [nchar](250) NULL,
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

