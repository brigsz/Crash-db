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
    [id] [int] NOT NULL,
    [date] [date] NULL,
    [vehicle_count] [int] NULL,
    [contributing_cause] [nchar](100) NULL,
    [alternate_cause] [nchar](100) NULL,
    [driver_condition] [nchar](100) NULL,
    [driver_distraction] [nchar](100) NULL,
 CONSTRAINT [PK_Driver] PRIMARY KEY CLUSTERED
(
    [id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


