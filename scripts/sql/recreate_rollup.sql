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
	[commercial_vehicle] [bit] NULL,
	[teenager] [bit] NULL,
	[elder] [bit] NULL,
	[dark] [bit] NULL,
 CONSTRAINT [PK_Rollup] PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


