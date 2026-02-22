export interface Organization {
  name: string;
  slug: string;
  tagline: string;
  description: string;
  ideas_url: string;
  website_url: string;
  irc_channel: string;
  contact_email: string;
  mailing_list: string;
  tech_tags: string[];
  topic_tags: string[];
  category: string;
  gsoc_page: string;
  has_ideas: boolean;
}

export interface IdeaSubpage {
  slug: string;
  title: string;
  source_url: string;
  content: string;
}

export interface OrganizationWithIdeas extends Omit<Organization, "has_ideas"> {
  ideas_content: string | null;
  ideas_subpages: IdeaSubpage[];
}

export interface SearchDocument {
  slug: string;
  name: string;
  tagline: string;
  description: string;
  ideasSnippet: string;
  tech_tags: string[];
  topic_tags: string[];
  subpageSlug?: string;
  orgName?: string;
}

export interface TagCount {
  tag: string;
  count: number;
}
