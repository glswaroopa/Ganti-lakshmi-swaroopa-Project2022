USE [Banking]
GO

/****** Object:  Table [dbo].[customers]    Script Date: 5/29/2022 5:20:18 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[customers](
	[Name] [char](100) NULL,
	[Address] [char](100) NULL,
	[PhoneNumber] [nvarchar](50) NULL,
	[Username] [nvarchar](50) NOT NULL,
	[Password] [nvarchar](50) NOT NULL,
	[intialBalance] [int] NULL,
	[AccountNumber] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Username] ASC,
	[AccountNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


